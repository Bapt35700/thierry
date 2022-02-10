import discord

from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions, MissingPermissions


musics = {}


bot = commands.Bot(command_prefix='!')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

warnings = {}


@bot.event
async def on_ready():
    print("bot prêt")


@bot.command()
async def regles(ctx):
    await ctx.send("regles: 1/ pas de spam 2/ ne pas upload d'images choquantes 3/ respecter les autres")

@bot.command()
async def bienvenue(ctx, nouveau_membre: discord.Member):

    pseudo = nouveau_membre.mention

    await ctx.send(f"Bienvenue à {pseudo} dans l'équipage du kraken ! N'oublie pas de regarder les règles en faisant: !regles")


@bienvenue.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("tu dois faire !bienvenue +@pseudo")




@bot.command()
async def python(ctx):
    await ctx.send("https://www.youtube.com/watch?v=psaDHhZ0cPs&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR")

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="ur prefix", intents=intents)

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.send("tu as été ban du serveur")
    await member.ban(reason=reason)
    await ctx.send(f'Thierry utilise coup de krâne, allez au revoir monsieur et madame tout le monde. {member} a été pulvériser par le coup de krâne de Thierry, il a donc été ban du serv')


@bot.command()
async def capitaine(ctx):
    await ctx.send("le capitaine de l'équipage est @SMiaths#1710")

@bot.command()
async def invitation(ctx, member : discord.Member):
    pseudo = member.mention
    await member.send("https://discord.gg/XCZ8cXSrC9")
    await ctx.send(f"salut {pseudo} je viens de t'envoyer en mp le lien d'invitation de discord, tu peux l'utiliser pour inviter des potes à toi !")


@invitation.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("tu dois faire !invitation et tu dois mentionner quelqu'un")

@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.send("tu as été kick du serveur discord, tu peux le rejoindre si tu veux : https://discord.gg/XCZ8cXSrC9")
    await member.kick(reason=reason)
    await ctx.send(f"{member} a été kick")




@kick.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("tu dois faire la commande !kick + un pseudo ")





@ban.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Tu dois faire !ban + un @pseudo")

@bot.command()
async def unban(ctx, *, member):

    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f"thierry accepte que {user} reste, il a été déban")
        return





@unban.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("tu dois faire la commande !unban + le bon pseudo correctement écrit ")

@bot.command()
async def chauve(ctx):
    await ctx.send('https://imgur.com/uwP19Qh')

@bot.command()
async def arabedelespace(ctx):
    await ctx.send('https://img.20mn.fr/oKqbosWSQrWBGsIgp4sDUQ/310x190_hazzaa-al-mansouri-premier-emirati-espace.jpg')



@bot.command()
@commands.has_permissions(administrator=True)
async def kingchokeur(ctx, member : discord.Member):
   pseudo = member.mention
   await ctx.send(f"et........................ le nouveau roi des chokeur est........... {pseudo} merci à toi de faire rater tous les vols athenas")
   await member.send(f"{pseudo} tu as été élu le roi des chokeur pour ça tu te prends un uppercute (coup de krâne , -30000000000000000000 de pv )")


@kingchokeur.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Tu dois faire !kingchokeur + un @pseudo")


@bot.command()
async def botpython(ctx, member : discord.Member):
    pseudo = member.mention
    await ctx.send(f"salut {pseudo} je t'ai envoyé la vidéo en mp")
    await  member.send(f"salut {pseudo} voici le lien : https://www.youtube.com/watch?v=m9CSCj7SkdM")


@botpython.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("pour que j'envoies la vidéo du bot discord en python, tu dois faire !botpython + @pseudo")

@bot.command()
async def commandes(ctx):
    await ctx.send("commandes : -!regles		-!bienvenue + @pseudo		-!python		-!ban + @pseudo			-!capitaine		-!invitation + @pseudo		-!kick + @pseudo		-!unban + pseudo#xxxx		-!botpython + @pseudo		-!commandes		-!clear			-!addrole + nom du role + id du membre à qui on veut ajouter le role (pour connaître les id des membres on utilise la commande: !idmembres)		-!removerole + nom du role + id du membre		-!idmembres		-!roles			-!damné + @pseudo		-!warn + @pseudo		-!name + @pseudo		-!site")

@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=2):
	await ctx.channel.purge(limit=amount)

@bot.command()
@commands.has_permissions(administrator=True)
async def addrole(ctx, role : discord.Role, user : discord.Member):
    await user.add_roles(role)
    await ctx.send(f" {user.mention} a obtenu le role {role.mention} ")
    await user.send(f"salut {user.mention} je te mp pour te dire que tu as reçu le role {role.mention} dans le serveur kraken ")

@addrole.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("pour pouvoir ajouter un role à un membre du serveur tu dois premièrement avoir les droits d'administrateur pour le faire et tu dois écrire la commande sous forme de : !addrole (nom du role) (id du membre à qui tu veu ajouter le role) par exemple on peut faire : !addrole Damné 694234858712596481 //////// ps !!!!! pour connaitre les id de tous les membres tu tape la commande !idmembres ")







@bot.command()
@commands.has_permissions(administrator=True)
async def removerole(ctx, role : discord.Role, user : discord.Member):
    await user.remove_roles(role)
    await ctx.send(f" {user.mention} a perdu  le role {role.mention}")
    await user.send(f"salut {user.mention} je te préviens que tu as perdu un role c'est pour cela que tu as des choses qui ont changé sur le serveur kraken")


@removerole.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("pour pouvoir enlever un role à un membre du serveur tu dois premièrement avoir les droits d'administrateur pour le faire et tu dois écrire la commande sous forme de : !removerole (nom du role) (id du membre à qui tu veu ajouter le role) par exemple on peut faire : !removerole Damné 694234858712596481 //////// ps !!!!! pour connaitre les id de tous les membres tu tape la commande !idmembres ")

@bot.command()
async def idmembres(ctx):
    await ctx.send("voici les id de tous les membres du serveur :  @Bapt35700 = 694234858712596481              @DICTATEUR = 540568372778369034             @pain d épice = 496737575051198465          @Spie35 = 650640523517886464            @petit_ours_brun = 724356626450087949           @BOT.EXE = 887378768765796362           @thierry = 860230245889605632           @barbenoire = 767015177610199101            ")

@bot.command()
async def cringe(ctx, member : discord.Member):
    pseudo = member.mention
    await ctx.send(f"enfin {pseudo} tu es cringe !")
    await member.send(f"salut {pseudo} j'ai vu que tu étais cringe alors tu te prends un uppercute batard")

@cringe.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("tu dois faire !cringe + @pseudo")


@bot.command()
async def roles(ctx):
    await ctx.send("les roles sur le serveur kraken sont :      -Capitaine : 836152787599228928     -Codeurs Pro : 835925820413181952       -BOT : 842399523493511198        -muted : 858725351562805288           -BOT.EXE : 905171799636050033       -thierry :  860230502975275019      -Damné : 872799673201598485          -Pirate-Chanceux : 906125873474863115            -Moussailons : 772424004602429440 ")




@bot.command()
async def damné(ctx, member: discord.Member):
    pseudo = member.mention
    await ctx.send(f"on est obligé de te donner le rôle @Damné {pseudo}car au cas ou tu ne respecte pas les règles on t'enlève le rôle Moussailons pour que tu sois Damné")

@damné.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("tu dois faire !damné + @pseudo")

@bot.command(pass_context=True)
@has_permissions(manage_roles=True, ban_members=True)
async def warn(ctx, member: discord.Member):
    pseudo = member.mention
    id = member.id
    print(id)

    if id not in warnings:
        warnings[id] = 0
        print("le membre n'a aucun avertissement")

    warnings[id] += 1
    print("ajout de l'avertissement", warnings[id], "/3")


    await ctx.send(f"attention {pseudo} tu as reçu 1 warn ! Respecte les règles du serveur stp ! {warnings[id]}/3")

    if warnings[id] == 3:
        warnings[id] = 0
        print("le membre a reçu trop de warns, il est Damné sur le serveur")
        role1 = get(member.guild.roles, name="Damné")
        role2 = get(member.guild.roles, name="Pirate-Chanceux")
        role3 = get(member.guild.roles, name="Moussailons")
        await member.remove_roles(role3)
        await member.add_roles(role1)
        await member.remove_roles(role2)
        await ctx.send(f"le membre {pseudo} est devenu Damné sur le serveur pour la raison : trop de warns !")


@warn.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("tu dois faire !Damné + @pseudo")
async def warn_error(self, ctx, error):
    if isinstance(error, error.MissingPermissions):
        await ctx.send("tu n'as pas les droits")


@bot.command()
async def name(ctx, member: discord.Member):
    await ctx.send(f"le vrai pseudo de {member.mention} est : {member}")



@bot.command()
async def site(ctx):
    await ctx.send("https://bapt35700.github.io/accueilkraken/")

@bot.command()
async def banniere(ctx, member: discord.Member):
    pseudo = member.mention
    await ctx.send(f"salut {pseudo} je t'ai envoyé le lien de téléchargement de la banniere kraken en mp ;)")
    await member.send("https://drive.google.com/u/0/uc?id=1i8We8J9afsrqmixEx5VG-n7azwF4XnC1&export=download")

@banniere.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("tu dois faire !banniere + @pseudo")


@bot.command(passcontext=True)
async def rename(ctx, member : discord.Member, nick):
   await member.edit(nick="[̷K̷̷R̷̷K̷] 爪ㄖㄩ丂丂卂丨ㄥㄖ几"+nick)
   await ctx.send(f"{member.mention} a changé de nom")
   print(f"{member} a changé de nom pour {nick}")
   await member.send(f"salut tu as changé ton pseudo sur kraken en {nick}")


@bot.command(passcontext=True)
async def mute(ctx, member: discord.Member):
    pseudo = member.mention
    role1 = get(member.guild.roles, name="Damné")
    role2 = get(member.guild.roles, name="Pirate-Chanceux")
    role3 = get(member.guild.roles, name="Moussailons")
    await member.remove_roles(role3)
    await member.add_roles(role1)
    await member.remove_roles(role2)
    await ctx.send(f"{pseudo} a été mute sur le serveur !")
    await member.send(f"salut {pseudo}, tu as été mute sur le serveur kraken !")

@mute.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("tu dois faire !mute + @pseudo")

@bot.command(passcontext=True)
async def unmute(ctx, member: discord.Member):
    pseudo = member.mention
    role1 = get(member.guild.roles, name="Damné")
    role2 = get(member.guild.roles, name="Pirate-Chanceux")
    role3 = get(member.guild.roles, name="Moussailons")
    await member.add_roles(role3)
    await member.add_roles(role1)
    await member.add_roles(role2)
    await ctx.send(f"{pseudo} a été unmute sur le serveur !")
    await member.send(f"salut {pseudo}, tu as été unmute sur le serveur kraken !")

@unmute.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("tu dois faire !unmute + @pseudo")
































































jeton = "ODYwMjMwMjQ1ODg5NjA1NjMy.YN4N2A.d9vZ5f6e-VQ1DHNbWyIjt5zrMS8"

print("lancement du bot...")



bot.run(jeton)