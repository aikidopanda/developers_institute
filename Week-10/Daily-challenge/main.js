const largeNumber = 356

function getDate(){
    const currentDate = new Date(); 

    let year = currentDate.getFullYear();
    let month = currentDate.getMonth() + 1; 
    let day = currentDate.getDate();

    let hours = currentDate.getHours();
    let minutes = currentDate.getMinutes();
    let seconds = currentDate.getSeconds();

    return [year, month, day, hours, minutes, seconds]
}

module.exports = { largeNumber, getDate }

