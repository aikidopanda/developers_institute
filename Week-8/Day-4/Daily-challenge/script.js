class Video{
    constructor(title, uploader, time){
        this.title = title
        this.uploader = uploader
        this.time = time
    }
    watch(){
        console.log(`${this.uploader} watched all ${this.time} of ${this.title}`)
    }
}
onlineLearningVideo = new Video('Learning', 'Steve', '18 mins')
anime = new Video('Spirited Away', 'John', '1 hour 40 mins')
onlineLearningVideo.watch()
anime.watch()