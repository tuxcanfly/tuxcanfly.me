Internship with Conformal Systems
#################################

:date: 2014-10-01 22:23
:tags: bitcoin
:category: general
:slug: internship-with-conformal-systems
:author: Javed Khan
:summary: Recap of my work during the internship

.. figure:: |filename|/images/bitcoin.png
   :align: left
   :alt: bitcoin
   :target: |filename|/images/bitcoin.png

.. figure:: |filename|/images/gopher.jpg
   :align: right
   :alt: gopher
   :target: |filename|/images/gopher.jpg

Almost six months ago I saw a blog post regarding bitcoin `internships`_ and I
was really excited for the opportunity, so I applied right away and was lucky
enough to get selected. Since then, it has been a tremendous learning
opportunity and thanks to the kind and helpful mentors at Conformal, I was able
to pickup a lot things and put them to use in the project. Also, thanks to my
fellow interns, I was able to get up to speed even though our schedules were
different.

.. _internships: https://blog.conformal.com/2014-summer-internships-hacking-on-bitcoin-with-go/

I started off with only a basic knowledge of both Bitcoin and Go. Most of my
previous experience with Bitcoin was from a payment backend I had added to
`django-merchant`_. To get a  better understanding, I tried to work with
`btcwire`_, which is at the lowest layer in the `btcd`_ suite. I started off
with a small `BIP implementation`_ for specifying user agents. Then I was able
to dig deeper and add support for `Alert`_ messages.

.. _django-merchant: http://agiliq.com/demo/merchant/
.. _btcwire: https://github.com/conformal/btcwire
.. _btcd: https://github.com/conformal/btcd
.. _BIP implementation: https://github.com/bitcoin/bips/blob/master/bip-0014.mediawiki
.. _Alert: https://en.bitcoin.it/wiki/Alerts

Next, I started working on the main project which is `btcsim`_. I came across
some issues with interrupt and I tried to debug and fix them. During this
process I reported issues with `btcd`_ and `btcwallet`_ related to clean
shutdown and tried to figure out and provide a patch whenever I could. Thanks
to the documenation and readability of both the packages, it was a breeze to
find out the issue and draft a patch.

.. _btcsim: https://github.com/conformal/btcsim
.. _btcwallet: https://github.com/conformal/btcwallet

To make it easier to monkey-test interrupts with long running processes like
btcsim, btcd and btcwallet I wrote a small util called `annyong`_.  Annyong
loves to annoy processes by interrupting them and seeing if they break.

.. _annyong: http://github.com/tuxcanfly/annyong

To describe btcsim in brief, it's a simulation test driver which simulates
growth of the blockchain in relation to the block size. A node is launched
first, which serves as a common node for all agents called Actors.  Then a
miner node is added as it's peer and mining begins. The input is read from a
CSV and the blocks are generated according to it. This helps us find out stats
like average number of transactions per second, maximumn number of transactions
per block, especially at large block sizes by using a high ``-blockmaxsize``
parameter.

After working on btcsim for a bit we were able to get transaction simulations
between actors working.  We found an issue where some transactions went missing
as they were created and available in the node mempool, but absent from the
miner mempool. After debugging using the trace logger in btcd, we found that it
was because of a `bug in the rate limiter`_ and were able to put together a
temporary patch.

.. _bug in the rate limiter: https://github.com/conformal/btcd/pull/160

Coming back to btcsim, we were able to speed up the transaction rate by using
``CreateRawTransaction`` in place ofe ``SendToAddress`` as the latter takes
time to calculates fees and does other things which were not necessary. This
also helped later in acheiving the desired UTXO count.

For matching the block height vs transaction count as per the given input
curve, we control the mining using the miner rpc client such that it only mines
when there are enough transactions in the mempool. Transactions are randomly
generated between actors by passing around addresses among each other. The
transaction input was earlier fetched using the API call ``ListUnspent`` but
since all the actors are under our control, we can simply keep track of the
UTXOs ourselves. This is done by listening to block notifications and fetching
the transactions involved, finding the owner and queueing the outputs. Using
this we were further able to speed up the simulation.

The last piece in the puzzle was to make sure we have enough UTXOs to generate
very large (~32MB) block sizes . I was able to acheive this by making some
calculations based no available UTXOs, finding how many are required and
generating transactions within the same actor such that the outputs are split
into smaller and smaller pieces and we end up with the required number of
UTXOs. Unfortunately with my limited hardware, I was only able to reach a
maximum of around 1,15,000 transactions per block and a maximum of 22MB block
size. Also, there is an issue because of which the simulation gets jammed after
a time. To make all such future issues reproducible without going through
hoops, I'm working on adding unit tests and making the system more predictable.

I was also able to get a part of the simulation working with bitcoind but the
lack of websocket notifications makes it difficult to integrate it with the
current implementation. It'd be great to have btcsim work with bitcoind as it
would provide us with insight into the different implementations.

So in retrospect, it has been a wonderful experience and a great opportunity to
explore bitcoin in detail. I've also come to like the simplicity of Go and
would love to continue working on both these technologies.

Once again I'd like to thank Conformal Systems for giving me this opportunity.
