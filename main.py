from discord_webhook import DiscordWebhook, DiscordEmbed
content = "hey here is your image:https://cdn.discordapp.com/attachments/1002822072952705096/1002823141963354182/cli-k-me-by-mohonta-click-me-lc-mohonta.gif"

webhook = DiscordWebhook(url="change me", username = "london image logger", content=content)

embed = DiscordEmbed(title="**image loggers are fake**", color=242424)

webhook.add_embed(embed)
response = webhook.execute()