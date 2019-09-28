fetch("https://hacknyapi.onrender.com/predict", {
    body: '{"Schooling": "16", "English": 0}',
    headers: {
      "Content-Type": "application/json"
    },
    method: "POST"
  }).then(res => res.text()).then(text => console.log(text))