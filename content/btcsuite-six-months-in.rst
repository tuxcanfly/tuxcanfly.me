btcsuite - six months in
########################

:date: 2015-04-01 22:23
:tags: job, tech, bitcoin, golang
:category: work
:slug: btcsuite-six-months-in
:author: Javed Khan
:summary: Recap of my work in the past six months

.. figure:: |filename|/images/btcsuite.png
   :align: left
   :alt: btcsuite
   :target: |filename|/images/btcsuite.png

With today I will be completing six months of working with the btcsuite team
and I want to write about some of the major work that I've been doing during
this time.

I've been working mostly on btcwallet which implements a bitcoin wallet and
provides all the functionality required by the end user to start receiving and
spending bitcoins.

Accounts:
=========

bitcoind has a notion of accounts for keeping track of ledgers of multiple
user-defined groups. They can be very useful for cases when a single wallet
instance needs to maintain balances for multiple users.

For example, consider a service provider that accepts prepaid credit, where
each customer can top-up and spend his credits. A wallet could create an
account for each customer and simply track the account balance. Security and
privacy would be important to make sure that no customer can access or steal
another customer's credits.

Unfortunately, the implementation of accounts in bitcoind is far from perfect
and this leads to a lot of "covering-up" in most of the account-related RPC
calls. Ideally, a wallet should treat each credit/debit as belonging to an
account and track them individually. Instead, bitcoind has a "bolt-on"
accounting system that leads to issues like "weird balances". Here's a `issue
on github`_ discussing this in more detail.

Previous versions of btcwallet only used the default account and did not
support multiple accounts. With the introduction of `waddrmgr`_, the new wallet
address manager, multiple account support became possible but it needed to be
integrated with the wallet core and the RPC server. 

I worked on this in `PR #155`_ and btcwallet now provides two new extension RPC
calls i.e `createaccount`, `renameaccount` which can be used to manage
accounts. Most of the account-related RPC calls are compatible with bitcoind in
that they work with accounts as expected.

.. _waddrmgr: https://github.com/btcsuite/btcwallet/pull/147
.. _issue on github: https://github.com/bitcoin/bitcoin/issues/3816
.. _PR #155: https://github.com/btcsuite/btcwallet/pull/155

Address Import:
===============

In case a user doesn't want to setup a wallet but just import a single address,
bitcoind provides the RPC call `importprivkey`. However, if the user just wants
to track the balance of the address, they should not need to provide the
private key. With btcwallet, one can do the same using the public key or just
the address itself. This feature is available using the two new extension RPC
calls `importpubkey` and `importaddress`. It was implemented in `PR #204`_ and
I'm currently working on adding tests for the database upgrade before it is
merged.

.. _PR #204: https://github.com/btcsuite/btcwallet/pull/204

Address Reuse:
==============

One of the major security concerns with bitcoin wallets is `address reuse`_.
Ideally an address must be not used once it's private key has been used to sign
a transaction. To prevent this, in `PR #207`_ I worked on flagging used
addresses so that it's easier to query and prevent address reuse.

.. _address reuse: https://en.bitcoin.it/wiki/Address_reuse
.. _PR #207: https://github.com/btcsuite/btcwallet/pull/207

wtxmgr:
=======

I worked on an initial version of the wtxmgr, the new transaction store, to
rewrite it to use walletdb backend instead of file backend. However, it also
required a rewrite in the way data is stored in boltdb compared to the older
file format for efficiency and is currently being worked on in `PR #217`_ by
jrick.

.. _PR #217: https://github.com/btcsuite/btcwallet/pull/217

Next steps:
===========

I've learnt a lot during the past six months and I hope to continue
contributing further to btcwallet and btcsuite. I think good code is never
complete without relevant docs and meaningful tests so I want to make it a
point to write better tests and docs. Also I'd like to make a regular post on
the latest work that's going on in `btcsuite`_

btcwallet is being actively worked on. You can see what's in store in the
`btcwallet roadmap`_, 

I'm most excited about SPV mode support as it means the user can start using
btcwallet without access to a full node.

If you're interested, you can check out the project on `github`_ or chat with
the team on `IRC`_

.. _btcsuite: https://github.com/btcsuite
.. _github: https://github.com/btcsuite/btcwallet
.. _IRC: https://opensource.conformal.com/wiki/IRC_server
.. _btcwallet roadmap: https://blog.companyzero.com/2015/03/btcwallet-0-5-0-release-and-roadmap/
