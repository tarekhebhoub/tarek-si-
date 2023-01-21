

document.querySelector('form').addEventListener('submit', (e) => {
  e.preventDefault();
  data={
    "code":e.srcElement[0].value,
    "nom_prenom":e.srcElement[1].value,
    "adresse":e.srcElement[2].value,
    "téléphone":e.srcElement[3].value
  }
  console.log(data)
  fetch("http://127.0.0.1:8000/clients/", {
      method: 'POST',
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(jsonData => console.log(jsonData))
    .catch((error)=>{
      console.log(error);
    })
});