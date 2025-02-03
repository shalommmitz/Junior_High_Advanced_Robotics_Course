** Target: create bootable disk-on-key that will remember changes and saved files

** Steps:
   
   1. Download the most recent LTS Ubuntu server ISO (E.g., 24.04)
   2. Write the ISO file to a disk_on_key (In Linux, use dd)
   3. Insert a 2nd disk-on-key to a PC (or laptop)
   4. Insert the 1st disk-on-key (with the ISO) to the same PC
   5. Boot the PC from the 1st disk-on-key
   6. Follow the prompts to install Ubuntu server on the 2nd disk-on-key
      WARNING: the default is to erase your PC hard-disk. Ma               Make SURE this does not happen. If in doubt, turn PC off
      Warning: this will erase everything on your 2nd disk-on-key
   7. Remove the 1st disk-on-key from the PC. You will not need it anymore
   8. Boot the PC so it will use the OS from the disk-on-key
      You might have to press F12 and/or adjust boot parameters in the BIOS
   9. At the Linux prompt execute:
      git clone https://github.com/shalommmitz/host_with_gui
      cd host_with_gui
      cd ansible
      ./INSTALL
      Feed your user password (that you set during installation) twice
   10. Reboot the PC
   11. Install essential packages:
   12 Customize to taste
