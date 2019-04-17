{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'warc'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-6-b31e7e5e2502>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mtime\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mtime\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mwarc\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mbs4\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mBeautifulSoup\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mselectolax\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mparser\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mHTMLParser\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'warc'"
     ]
    }
   ],
   "source": [
    "from time import time\n",
    "\n",
    "import warc\n",
    "from bs4 import BeautifulSoup\n",
    "from selectolax.parser import HTMLParser\n",
    "import wget"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "main_url = \"https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2019-13/segments/1552912201672.12/warc/CC-MAIN-20190318191656-20190318213656-00398.warc.gz\"\n",
    "warc_file = wget.download(main_url)\n",
    "file_name =  \"crawl-data/CC-MAIN-2019-13/segments/1552912201672.12/warc/CC-MAIN-20190318191656-20190318213656-00398.warc.gz\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_text_bs(html):\n",
    "    tree = BeautifulSoup(html, 'lxml')\n",
    "\n",
    "    body = tree.body\n",
    "    if body is None:\n",
    "        return None\n",
    "\n",
    "    for tag in body.select('script'):\n",
    "        tag.decompose()\n",
    "    for tag in body.select('style'):\n",
    "        tag.decompose()\n",
    "\n",
    "    text = body.get_text(separator='\\n')\n",
    "    return text\n",
    "\n",
    "\n",
    "def get_text_selectolax(html):\n",
    "    tree = HTMLParser(html)\n",
    "\n",
    "    if tree.body is None:\n",
    "        return None\n",
    "\n",
    "    for tag in tree.css('script'):\n",
    "        tag.decompose()\n",
    "    for tag in tree.css('style'):\n",
    "        tag.decompose()\n",
    "\n",
    "    text = tree.body.text(separator='\\n')\n",
    "    return text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "urllist[]\n",
    "def read_doc(record, parser=get_text_selectolax):\n",
    "    url = record.url\n",
    "    text = None\n",
    "    urllist.append(url)\n",
    "    return urllist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def process_warc(file_name, parser, limit=10000):\n",
    "    warc_file = warc.open(file_name, 'rb')\n",
    "    t0 = time()\n",
    "    n_documents = 0\n",
    "    for i, record in enumerate(warc_file):\n",
    "        urllist = read_doc(record, parser)\n",
    "\n",
    "        n_documents += 1\n",
    "\n",
    "        if i > limit:\n",
    "            break\n",
    "\n",
    "    warc_file.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100% [......................................................................] 964192996 / 964192996"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'CC-MAIN-20190322115048-20190322141048-00227.warc.gz'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import wget\n",
    "exurl =\"https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2019-13/segments/1552912202658.65/warc/CC-MAIN-20190322115048-20190322141048-00227.warc.gz\"\n",
    "wget.download(exurl)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
