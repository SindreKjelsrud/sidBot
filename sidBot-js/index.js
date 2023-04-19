const axios = require('axios');

const { Client, GatewayIntentBits, EmbedBuilder, PermissionsBitField, Permissions, ActivityType, AttachmentBuilder, ALLOWED_EXTENSIONS } = require(`discord.js`);
const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent] });
// const welcome = require(`./welcome.js`); ~ not working

const prefix = '!';
const TOKEN = 'REMOVED FOR SECURITY REASONS';

// ********* BOT READY ********* //
client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);

    // welcome(client); ~ not working

    client.user.setActivity('!help', { type: ActivityType.Playing });
})

// ********* MESSAGE RESPONSES ********* //
client.on("messageCreate", (message) => {
    if(!message.content.startsWith(prefix) || message.author.bot) return;

    const args = message.content.slice(prefix.length).split(/ +/);

    const command = args.shift().toLowerCase();

    // message array
    const messageArray = message.content.split(" ");
    const argument = messageArray.slice(1);
    const cmd = messageArray[0];

    // ********* COMMANDS ********* //
    // help -> shows all commands + description of each
    if (command === 'help') {
        const commandtext = '!help \n - List of commands \n\n' +
                    '!hello \n - Bot responds with "Hello!" \n\n' +
                    '!ping \n- Bot responds with "Pong!" and botlatency + a gif from Ping Pong The Animation \n\n' +
                    '!github \n- Flexes github link \n\n' +
                    '!coinflip\n- Heads or Tails! \n\n' +
                    '!invbot\n- Bot sends invite link for itself' +
                    '!xmas\n- Someone writes "merry christmas" and bot responds w/ legendary vine quote selected from an array \n\n' +
                    '!dog\n- Bot supplies with pictures of cute doggos across the whole internet through Dog API \n\n' +
                    '!quote\n- Bot inspires user with a quote from the free, open source quotations API Quotable \n\n' +
                    '!kanye\n- Bot gives user a legendary Kanye quote \n\n' +
                    '!chuck norris\n- Bot gives user a good old Chuck Norris joke \n\n' +
                    '!btc\n- Bot shows user current Bitcoin price in euro \n\n' +
                    '!eth\n- Bot shows user current Ethereum price in euro \n\n' +
                    '!meme\n- Bot summons a random meme from reddit';
        const embedVar = new EmbedBuilder()
            .setColor(0x7B64FF)
            .setTitle('List of sidBots features/commands:')
            .addFields({ name: ':volcano: Commands:', value: commandtext, inline: true});
        message.reply({ embeds: [embedVar] });
    }

    // hello
    if (command === 'hello') {
        message.reply("Hello!");
    }

    // ping
    if (command === 'ping') {
        const file = new AttachmentBuilder('./resources/pingpong.gif');
        message.channel.send(`Pong :ping_pong: (Bot latency: **${Math.round(client.ws.ping)}ms**)`);
        message.channel.send({ files: [file] });
    }

    // github
    if (command === 'github') {
        message.reply("https://github.com/SindreKjelsrud");
    }

    // coinflip
    if (command === 'coinflip') {
        const coinflip = ['```Heads```', '```Tails```']
        let answer = coinflip[Math.floor(Math.random() * coinflip.length)];
        const file = new AttachmentBuilder('./resources/coinspin.gif');
        message.channel.send({ files: [file] });
        // sleep(2000); // ~ have to fix sleep
        message.channel.send(answer);
    }

    // xmas response
    if (command === 'xmas') {
        const xmasAnswers = ['Happy Chrismis!', 'Its Chrismin!', 'Merry Chrisis!', 'Merry Chrysler!'];
        let answer = xmasAnswers[Math.floor(Math.random() * xmasAnswers.length)];
        message.reply(answer);
    }

    // invbot
    if (command === 'invbot') {
        message.reply("https://discord.com/api/oauth2/authorize?client_id=1054491638682095626&permissions=8&scope=bot");
    }

    // 8ball
    if (command === '8ball') {
        const facts = [`Yes`, `No`, `Maybe`];
        let fact = facts[Math.floor(Math.random() * facts.length)];
        message.reply(fact);
    }
    
})

// ********* API MESSAGE RESPONSES ********* //
client.on("messageCreate", async (melding) => {
    // quote
    if (melding.content === '!quote') {
        let resp = await axios.get('https://api.quotable.io/random');
        const quote = resp.data.content;

        melding.reply({
            content: quote,
        })
    }

    // kanye
    if (melding.content === '!kanye') {
        let resp = await axios.get('https://api.kanye.rest');
        const quote = resp.data.quote;

        melding.reply({
            content: quote,
        })
    }

    // dog
    if (melding.content === '!dog') {
        let resp = await axios.get('https://dog.ceo/api/breeds/image/random');
        const doggo = resp.data.message;
        const dogTitles = ['Who let the dogs out?:dog:', 'woof:dog:', 'Whos a good boy!:dog:', 'meow:cat:', 'Mr. GoodBoy:dog:', 'Bork Bork!:dog:']
        let answer = dogTitles[Math.floor(Math.random() * dogTitles.length)];
    
        const dogEmbed = new EmbedBuilder()
            .setTitle(answer)
            .setImage(doggo)

        melding.reply({
            embeds: [dogEmbed],
        })
    }

    // chuck norris joke
    if (melding.content === '!chuck norris') {
        let resp = await axios.get('https://api.chucknorris.io/jokes/random');
        const norris = resp.data.value;
    
        melding.reply({
            content: norris,
        })
    }

    // bitcoin
    if (melding.content === '!btc') {
        let resp = await axios.get(`https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur`);
        const price = resp.data.bitcoin.eur;
    
        melding.reply({
            content: "Current price of Bitcoin: " + price + "£",
        })
    }

    // ethereum
    if (melding.content === '!eth') {
        let resp = await axios.get(`https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=eur`);
        const price = resp.data.ethereum.eur;
    
        melding.reply({
            content: "Current price of Ethereum: " + price + "£",
        })
    }

    // meme
   if (melding.content === '!meme') {
        let resp = await axios.get('https://meme-api.com/gimme');
        const img = resp.data.preview[3];

        melding.reply({
            content: img,
        })
   }

})


client.login(TOKEN);