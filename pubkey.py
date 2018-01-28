#! python3
#this is a python program for loading public keys for wallets

import sys
import pyperclip

KEYS = {'mew': '0xdc98a02595c7799342181227F04C223a6C2049a1',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}


if len(sys.argv) < 2:
    print('Usage: python pubkey.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]      # first command line arg is the account name

if account in KEYS:
    pyperclip.copy(KEYS[account])
    print('Public key for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
    