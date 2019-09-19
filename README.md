Cashkey: A bank on your $5 USB stick 
==============================================

**cashkey** is a tool that helps you create a secure Bitcoin cash wallet on any USB flash drive and perform transactions using a CLI.

It creates an encrypted file (`key.enc`) on your USB flash drive containing your Bitcoin cash private key. To perform any operation, you'll have to enter your previously registred password. Otherwise, any operation is impossible.

Installation
------------

It's as simple as:
```bash
$ pip install cashkey
```

Usage
------------

**Important:** **cashkey** isn't as secured as a REAL hardware wallet, so don't use it as your main way to store your Bitcoins!

Before you start using **cashkey**, you have to format a USB flash drive to any format you want (preferably FAT32 for portability) and rename the key to `BCH` on formating.

Once done, go to your command line and run:
```bash
$ cashkey
```
You will then be invited to create a new password for your wallet. Choose a strong password and remember everyone with access to your USB wallet, your password and **cashkey** has access to your Bitcoins.

After creating a password, you'll be asked to re-run the program. Then to enter your password again. When done, you will have access to a prompt with the following options:

```
1 – Print your Bitcoin cash address
2 – Get your wallet balance in a given currency
3 – Get your transaction history
4 – Make a transaction
5 – Get transaction fees in satoshis per byte
6 – Create a new wallet
0 – Exit
```
You can then select an options by entering the **corresponding number** followed by **return**.

About
------------
My vision is to create a simple way for people who cannot afford a hardware wallet such as the [Ledger](https://www.ledger.com/) or the [Trezor](https://trezor.io/) to carry their cryptocurrencies in a secure way.
The long-term goal is to establish a universal protocol or convention to create a hardware wallet and access it with any software. Monopoly isn't something we should support in the crypto space, instead we should focus on making things simpler and open for everyone.

Based on community needs and demands, I will keep improving the project and adding new functionalities. You can help me do that by **contributing** to the project or by **donating** a little something to encourage me.

**Donate BCH:** bitcoincash:qrxjktfjdse3ll0ttrll20gykuhqjw764queg3w2tj

**Donate Love:** Just [tweet](https://twitter.com/merwanedr) me something cool :)

Contributing
------------
If you like **cashkey** so much that you want to contribute to it, you can make a pull request on a new branch wether it is for a bugfix or for a new feature. 

You can also request a feature or report a bug by using Github issues, or by dropping me an [email](mailto:merwanedr@gmail.com) if you're not technical.

Promoting the project is also considered a huge contribution! Any action is welcome as long as it helps **cashkey** grow! 

Notes and credits
------------
* I really wanted to thank [Ofek Lev](https://github.com/ofek) for his library [bit](https://github.com/ofek/bit) and [Sporestack](https://github.com/sporestack) with his fork [bitcash](https://github.com/sporestack/bitcash) which made **cashkey** possible without me having a headache, your libraries rocks!

* I tested **cashkey** on MacOS and Linux but I don't know if it works well on Windows. It would be cool if one of you contributors can test it and create an issue if it doesn't work properly.
