import subprocess


KERNEL_TO_INSTALL = 'linux'


subprocess.run(['clear'])
print('Arch Install Script')

setupWifi = input('Are you using Wi-Fi? (y/n) ').strip()
if setupWifi == 'y':
    print('Setting up Wi-Fi...')
    subprocess.run(['ip', 'link'])
    subprocess.run(['iwctl'])
else:
    print('Setting up Ethernet...')
    subprocess.run(['ip', 'link'])

print('Testing connection...')
print('Use Ctrl-C to exit.')
subprocess.run(['ping', 'archlinux.org'])

print('Install complete. Enjoy!')