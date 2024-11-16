import subprocess


KERNEL_TO_INSTALL = 'linux'


subprocess.run(['clear'])
print('Arch Install Script')

print('')
setupWifi = input('Are you using Wi-Fi? (y/n) ').strip()
if setupWifi == 'y':
    print('Setting up Wi-Fi...')
    subprocess.run(['ip', 'link'])
    subprocess.run(['iwctl'])
else:
    print('Setting up Ethernet...')
    subprocess.run(['ip', 'link'])

print('')
print('Testing connection...')
subprocess.run(['ping', '-c', '1', 'archlinux.org'])

print('')
print('Install complete. Enjoy!')