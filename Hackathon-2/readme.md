This is a small game-like website that can be used both for educational and entertainment purposes.

![Hackathon-2](https://github.com/aikidopanda/developers_institute/assets/31676788/fd8474d5-0043-417b-b16b-a003f41b4ac7)

How to launch:
1. Add your database settings in db_operations.js 'sequelize' and 'client' variables. Currently I removed my db password from project settings.
2. Uncomment syncModels() and populateDatabase() functions in db_operations.js.
3. Run db_operations.js (node db_operations.js).
4. Run server.js (node server.js). Press the link node will give you.

How to play:
1. Enter your name, then press 'play' in the main menu
2. The game is based on the set of questions and countdown timer. You will get one random question from database at a time.
3. If your answer is correct, you get bonus time.
4. If your answer is not correct or you didnt answer(the answer input is empty), you will get the next question, timer will continue to tick.
5. When you answer all the questions OR timer reaches 0, you will get your final score, depending on the percent of the questions you manage to give the correct answer.

Important:
1. The answer input is case-insensitive. Answers 'Roman Empire' or 'roman empire' will be the same for the program.
2. Some questions have multiple correct answers, you can write any of them.
3. The arabic and roman numbers are NOT the same. You should write roman numbers with monarchs' names (as its conventional) and arabic numbers in all other cases.

If I continue to work on this website, i'll add the GUI for adding questions and other user-friendly functions.




