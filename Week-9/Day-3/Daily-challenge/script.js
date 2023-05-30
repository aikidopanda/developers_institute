// API key: hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My

let myForm = document.forms[0] // choose form
let fields = myForm.elements; // choose all form fields

myForm.addEventListener("submit", submit);

async function submit(event) {
  event.preventDefault();
  if (fields[0].value.length > 0)
  {
    let info = {
      topic: fields[0].value,
    };

    let url = `https://api.giphy.com/v1/gifs/random?q=${info.topic}&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`

    let response = await fetch(url);
    if (response.status == 200)
    {
      const json = await response.json();

      gifSection = document.querySelector('section')
      for (item of gifSection.children){
        gifSection.removeChild(item)
      }

      let newImg = document.createElement("img");
      newImg.src = json.data.images.original.url;
      document.querySelector("section").appendChild(newImg);
    }
    else
    {
      throw new Error("bad query");
    }
  }
}