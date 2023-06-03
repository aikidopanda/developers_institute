const fs = require('node:fs') // importing necessary tools
const ejs = require('ejs')
const { Client } = require('pg')
const { Sequelize } = require('sequelize');
const express = require('express')
const app = express()
const db = require('./db_operations')

let timer = 150 //creating a countdown timer: you can set any value but it will affect the difficulty of the game
// for medium difficulty i recommend to set timer = total number of questions * 5
let score = 0 //every time player gives a correct answer his/her score increases
let playerName
let displayed = "Let's start!" // dynamic message displayed to player, changing during the game

app.get('/countdown', (req, res) => {
  let timer = playerTimer();
  res.json(timer);
});

function playerTimer() {
  if (timer > 0){
    timer--
  }
  return { seconds: timer };
}

app.use(express.static('public',//adding frontend js
{
  setHeaders: (res, path) => {
    if (path.endsWith('.js')) {
      res.setHeader('Content-Type', 'text/javascript');
    }
  }
}))
app.use(express.urlencoded({ extended: true }));

const hostname = '127.0.0.1'
const port = 3000

let questionsArray = []
let currentQuestion
getQuestions().then(result => {
  for (item of result){
    questionsArray.push(item)
  }
})

const serverMain = app.get('', (request, response) => {
  fs.readFile('main.ejs', 'utf-8', (err, template) => {
    if (err) {
      console.error('Error reading template:', err);
      return;
    }

    playerName = request.query.player

    let nameError = ''

    if ( playerName == ''){
      nameError = 'Please enter your name!'
    }
    else if (playerName != undefined){
      return response.redirect('/game')
    }

    let data = {
      nameError: nameError,
      questionDisp: displayed
    }

    let rendered = ejs.render(template, data)
    response.end(rendered)
  })
})


const server = app.get('/game', (request, response) => {
  let checkedResult
  fs.readFile('index.ejs', 'utf8', (err, template) => {
    if (err) {
      console.error('Error reading template:', err);
      return;
    }

    let userAnswer = request.query.answer

    if (userAnswer != undefined){
      let checked = checkAnswer(userAnswer,currentQuestion.answer)
      if (checked == true){
        checkedResult = 'Correct! You got +5 seconds'
        timer += 5
        score++
        currentQuestion.status = 1
      }
      else{
        checkedResult = 'Incorrect!'
        currentQuestion.status = 2
      }
    }

    currentQuestion = getRandom(questionsArray)
    if (currentQuestion == undefined || timer <= 0){
      displayed = finalScore(score)
      uploadResults(score)
      return response.redirect('/')
    }
    else{
      displayed = currentQuestion.text
    }

    const data = {
      questionDisp: displayed,
      userTimer: timer,
      result: checkedResult,
    };

    let renderedHTML = ejs.render(template, data);
    response.end(renderedHTML)
  });

  // response.writeHead(200, { "Content-Type": "text/html" })
})

if (server) {
  server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`)
  })
}


async function getQuestions() { //getting all the questions from database
  try{
      let questions = await db.Question.findAll(
        {
          attributes: { exclude: ['id', 'createdAt', 'updatedAt'] },
        }
      )
      return questions 
  }
  catch (error) {
    console.error('Error retrieving questions:', error);
  }
}
    
function getRandom(array) { //getting a random question which was not answered by the player yet
  let filtered = array.filter(question => question.dataValues.status == 0)

  if (filtered.length > 0){
    let index = Math.floor(Math.random() * filtered.length)
    let data = filtered[index].dataValues
    return data
  }
  
}

function checkAnswer(user, correct){
  let splitted = correct.split(';')
  let processed = []
  for (item of splitted){
    processed.push(item.toLowerCase())
  }
  if (processed.includes(user.toLowerCase())){
    return true
  }
  else{
    return false
  }
}

function finalScore(score){
  let questionsTotal = questionsArray.length
  let scoreFinal = score/questionsTotal * 100 
  let msg = `You answered ${score} questions of ${questionsTotal}. `
  if (scoreFinal > 0.75){
    msg += 'Your knowledge of world history is truly great! I suppose you have studied humanities in university. Or just read a lot of books:)'
  }
  else if (scoreFinal > 0.5){
    msg += 'You definitely have a good erudition in history. Probably you didnt study it professionally, but you had strong enthusiam to it'
  }
  else if (scoreFinal > 0.25){
    msg += 'You might have read historical novels or watched history-related films. Or you havent forgot your school knowledge yet:)'
  }
  else{
    msg += 'Looks like history knowledge is not your strong point. Probably you should start with reading popular books or playing history-related videogames:)'
  }
  return msg
}

async function uploadResults(score){
  let questionsTotal = questionsArray.length
  let scoreFinal = score/questionsTotal * 100 
  let newScore = await db.Score.create(
    {
      player: playerName,
      score: scoreFinal
    }
  )
  await newScore.save()
}

