// Here I placed the functions which are used to create a base of questions. 

// to drop the existing tables and create it again call syncModels() function
// to add new questions to the database, edit questions and answers array and call populateDatabase() function. call syncModels() first to prevent getting the same question multiple times
// then run the file -> node db_operations.js

const { Client } = require('pg')
const { Sequelize } = require('sequelize');

const sequelize = new Sequelize('Home', 'postgres', '', {
    host: 'localhost',
    dialect: 'postgres',
});

const client = new Client({
    user: 'postgres',
    host: 'localhost',
    database: 'Home',
    password: '',
    port: '5432',
});

const Question = sequelize.define('Question', {
    text: {
      type: Sequelize.TEXT,
      allowNull: false
    },
    answer: {
      type: Sequelize.STRING,
      allowNull: false
    },
    status: {
      type: Sequelize.SMALLINT,
      defaultValue: 0
    }
});

const Score = sequelize.define('Score', {
  player: {
    type: Sequelize.STRING,
    defaultValue: 'Guest'
  },
  score: {
    type: Sequelize.FLOAT
  }
});

async function syncModels() {
  await sequelize.sync({ force: true });
  console.log('Database models synchronized');
}

function tableCreating() {
    client.connect()
    client.query(
      `CREATE TABLE Questions(id serial primary key, text varchar(1000), answered integer default 0)`,
      (err, res) => {
        if (err) {
          console.error(err);
        } else {
          console.log('Table created successfully');
        }
      }
    )
    client.end
}

//populating database with questions

let questions = [
    'One ambitious nation called this sea Mare Nostrum, which literally means Our Sea. Write the modern name of this sea',
    'This European war lasts between 1618 and 1648 years. The dates can give you a hint.',
    'This dynasty of Manchu origins ruled China between 17th and 20th century. Write the name of this dynasty.',
    'This lame ruler of 14th century succeeded to build a great empire of Central Asia. Write his name.',
    'This legendary Shumer king became a hero of the whole epos, which covers a lot of events which are also mentioned in Bible. Write the name of this king.',
    'He was the last Russian tsar of Romanov family. In 1918 he and his family were shooted by Bolsheviks. Write his name and number.',
    'This empire, whose core lands covered the territory of modern Turkey, existed between 14th and 20th century. Write its name.',
    'This Native American people by the time of Spanish arrival ruled the large empire, covering all the territory of modern Peru, Bolivia and Equador.',
    'This famous mausoleum was build in 17th century by the order of Shah Jahan in memory of his favourite wife. Write the name of this monument.',
    'This legendary hero of Greek and later Roman mythology was known by his extreme strength and half-god origin. Write his name.',
    'This two countries (existing today) in 1494 signed the treaty, separating non-Christian world by a meridian. The mediator of this treaty was the Pope himself. Write these two countries, separated by comma.',
    'This French-origin word became the name of a political movement in 19th-20th century. The aim of this movement was granting voting right for women.',
    'These two African countries (existing today) were the only two countries of the whole continent who managed to maintain political independence after so-called Scramble for Africa in late 19th-early 20th century. Enter their modern names, separated by comma.',
    'Rock-festival in this small town in New York State, held in 1969, became one of the symbols of hippies and sexual revolution. Write the name of the city.',
    'Ironically, first (legendary) and last ruler of Ancient Rome had the same name. Write this name.',
    'The 1st World War, also known as Great War, started when Austria-Hungary declared war on...(write the name of this country)',
    'These two former Soviet republics, despite being the integral part of Soviet Union, had their own vote right at the United Nations Assembly. Write their names separated by comma.',
    'In 1966 he became the first Israeli who won Nobel Prize in literature.',
    'This document of British diplomacy de-facto became one of the most important milestones of re-creation Jewish state in Palestine',
    'This journalist and politician in 1897 founded the World Zionist Organization. Almost every modern Israeli city or town has a street named after him.',
    'This religion, founded in the 7th century A.D., is considered to be the youngest of so-called Universal Religions.',
    'The war between aristocratic houses of Yorks and Lancasters in medieval England, which inspired George Martin for writing his Game of Thrones series, was given quite poetical name. Write this name.',
    'This was a name of Dutch-origin colonists in South Africa, whose republics were crushed by the British army in the early 20th century.',
    'This drink, extremely popular over the world, became known in Europe mostly by chance. After defeating Turks in battle of Vienna in 17th century victorious Austrian and Polish soldiers plundered enemy camp and discovered a curious trophy. Write the name of this drink.',
    'This country is currently divided by 38 parallel, as a result of 3-year fierce war. Both parts are still pretending to represent the whole nation.',
    "This is the only country in the world, which survived nuclear strike. Let's hope that no one will ever join this club...",
    'Although Shiite branch of Islam is wide-spread in several countries, only one country has it as acknowledged state religion. Write the name of this country.',
    'This Swedish diplomat is known for saving thousand of Hungarian Jews during the Holocaust. Unfortunately, after the defeat of Nazis he was imprisoned by Soviets and allegedly died in Lubyanka prison in Moscow.',
    'This Greek philosopher was sentenced to death in 399 B.C. He is known as first historical figure who was put on trial and found guilty only for speaking. After being sentenced to death, he enforced the sentence himself by drinking poison.',
    "During the cold war this city was divided. Its Western part, controlled by Western bloc, was surrounded by territories controlled by Soviet bloc. Thats why this city was often called 'The capital of intelligence services'."
  ]

  let answers = [
    'Mediterranean;Mediterranean sea',
    '30-year;30-year war;Thirty-year;Thirty-year war',
    'Qing;Qing dynasty',
    'Timur;Tamerlan',
    'Gilgamesh',
    'Nicholas II',
    'Ottoman;Ottoman Empire',
    'Inca;Incas',
    'Taj Mahal;Taj-Mahal',
    'Hercules',
    'Spain,Portugal;Spain, Portugal',
    'Suffragette;Suffragist;Suffragettes',
    'Liberia, Ethiopia;Liberia,Ethiopia',
    'Woodstock',
    'Romul',
    'Serbia',
    'Ukraine, Belarus;Ukraine,Belarus',
    'Shmuel Agnon;Shmuel Yosef Agnon',
    'Balfour Declaration;The Balfour Declaration',
    'Herzl;Theodor Herzl',
    'Islam',
    'War of the Roses;War of Roses;Roses war',
    'Boers;Boer;Afrikaner;Afrikaners',
    'Coffee',
    'Korea',
    'Japan',
    'Iran',
    'Wallenberg;Raoul Gustaf Wallenberg;Raoul Wallenberg',
    'Socrates',
    'Berlin',
  ]
  
async function populateDatabase() {
    for (i = 0; i < questions.length; i++) {
      let question = await Question.create(
        {
          text: questions[i],
          answer: answers[i]
        }
      )
      await question.save()
    }
}

module.exports = { Client, Question, Score }

// syncModels()
// populateDatabase()

