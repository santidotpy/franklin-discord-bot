# franklin-discord-bot

![](https://i.imgur.com/Xt2KRRf.png) [**Add me to your server!**](https://discord.com/api/oauth2/authorize?client_id=845142608941547520&permissions=532576468032&scope=bot "Add me!")

Franklin es un bot para realizar consultas sobre el precio del dolar (blue, tarjeta, oficial), cryptos y el valor final de un producto con la carga impositiva en Argentina. **Migrando de Heroku**.               
**El prefijo para los comandos de Franklin es: `?`**

*(En Argentina tenemos muchos precios para el dolar y muchos impuestos)* 


------------


### Comandos

- **`?ben`**: proporciona un mensaje de ayuda con los comandos que se pueden usar con    	 Franklin
- **`?blue`**: devuelve el valor del dolar blue actual
- **`?tarjeta`**: devuelve el valor del dolar tarjeta actual
- **`?oficial`**: devuelve el valor del dolar oficial actual
- **`?usdars`**: convierte un valor dado en USD a ARS (precio blue). Ej: `?usdars 100`
- **`?usdt`**: devuelve el valor en ARS del USDT en distintos exchanges
- **`?tax`**: convierte un monto dado al precio que tendria incluyendo los impuestos que se aplicarian. Ej: el valor de un producto en Steam expresado en pesos no contempla los impuestos que el comprador pagaria `?tax 2500`
- **`?price`**: devuelve el precio de una crypto dada y un grafico de candlesticks. Por defecto este valor lo expresa en USDT pero puede especificarse en alguna otra coin. Ej: `?price btc usdc` para obtener el valor de Bitcoin expresado en USDC. Otro ejemplo: `?price eth` para obtener el valor de Ethereum en USDT
- **`?bio`**: devuelve un mensaje para conocer un poco sobre la vida de **[Benjamin Franklin](https://es.wikipedia.org/wiki/Benjamin_Franklin "Benjamin Franklin")**.   Por defecto el mensaje es en español, `?bio eng` para obtener el mensaje en ingles


------------


