#!/usr/bin/env python3

import os, sys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import config
from callbacks import start_cb, help_cb, error_cb, restart_cb, text_handler, signal_handler
from Listener import Listener

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print('usage: bot.py <kernel> <TOKEN>')
		sys.exit(0)
	else:
		kernel = sys.argv[1]
		token = sys.argv[2]
		if kernel not in config.kernels:
			print('Kernel %s not found; available kernels: %s' %(kernel, config.kernels))
			sys.exit(0)
		config.kernel = kernel
		config.kernel_name = config.kernel_names[kernel]

	os.makedirs('/home/jovyan/work', exist_ok=True)
        
	updater = Updater(token, use_context=True, user_sig_handler=signal_handler)

	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start_cb))
	dp.add_handler(CommandHandler("help", help_cb))
	dp.add_handler(CommandHandler("restart", restart_cb))
	dp.add_handler(MessageHandler(Filters.text, text_handler))
	dp.add_error_handler(error_cb)

	updater.start_polling()
	updater.idle()
