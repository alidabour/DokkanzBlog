from channels import Group
import json

def ws_connect(message):
	message.reply_channel.send({"accept": True})
	Group('users').add(message.reply_channel)

def ws_disconnect(message):
	Group('users').discard(message.reply_channel)

def ws_post_list_update(message):
	Group('users').send({
		'text': message.content['text']
	})

def ws_post_connect(message,post_id):
	message.reply_channel.send({"accept": True})
	Group("post-%s" % post_id).add(message.reply_channel)
	print("connect to post-%s" % post_id)

def ws_post_disconnect(message,post_id):
	Group('post-%s' % post_id).discard(message.reply_channel)
	print("disconnect from post-%s" % post_id)

def ws_post_update(message,post_id):
	print("\nupdate post----\t\t---\n")
	Group('post-%s' % post_id).send({
			'text': message.content['text']
		})
	