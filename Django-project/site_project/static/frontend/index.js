fetch("http://localhost:8000/api/site/categories/",{method:"GET"}).then((function(t){return t.json()})).then((function(t){console.log(t)})),axios.get("http://localhost:8000/api/site/products/").then((function(t){console.log(t.data)}));