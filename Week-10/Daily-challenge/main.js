const largeNumber = 356

function getDate(){
    const currentDate = new Date(); 

    let yearCur = currentDate.getFullYear();
    let monthCur = currentDate.getMonth() + 1; 
    let dayCur = currentDate.getDate();

    let hoursCur = currentDate.getHours();
    let minutesCur = currentDate.getMinutes();
    let secondsCur = currentDate.getSeconds();

    return {
        year: yearCur,
        month: monthCur,
        day: dayCur,
        hour: hoursCur,
        minute: minutesCur,
        second: secondsCur
    }
}

module.exports = { largeNumber, getDate }

