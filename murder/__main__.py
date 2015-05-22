#!/usr/bin/env python

import plac

def make(infile, outfile, host):
	if (infile != None and outfile != None and host != None):
		from .make import make as _make
		_make.make(infile, outfile, host)
	else:
		print("Required params are infile, outfile and host. See -h for help")

def track(port):
	print("Staring tracker on port " + str(port))
	from .tracker import tracker
	tracker.run_app(int(port))

@plac.annotations(
	command=('Mode', 'positional', None, str, ['make', 'track', 'client']),
	infile=('INFILE', 'option', 'i'),
	outfile=('OUTFILE', 'option', 'o'),
	host=('tacker host', 'option', 'H'),
	port=('listen port', 'option', 'p')
)
def main(command, infile, outfile, host='localhost:8080', port='8657'):
	"""
	Murder - The collective noun for a group of crows

	This tool helps you do large scale server bin depoys over the bittorrent protocal
	"""
	args = []
	{
		'make': lambda: make(infile, outfile, host),
		'track': lambda: track(port),
		'client': lambda: print("Starting in client mode")
	}[command]()

if __name__ == '__main__':
	plac.call(main)
