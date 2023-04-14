module.exports = client => {

    client.on("guildMemberAdd", member => {

        const channelID = 'X';

        console.log(member)

        const message = `**Welcome to the server, <@${member.id}>!**`;

        const channel = member.guild.channels.cache.get(channelID);

        channel.send(message);

    })

}