import subprocess


KERNEL_TO_INSTALL = 'linux'


subprocess.run(['clear'])
print('Arch Install Script')

print('Setting up Wi-Fi...')
subprocess.run(['ip', 'link'])
subprocess.run(['iwctl'])