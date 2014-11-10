devops-certifyme
================

Get DevOps certified now!  Like, RIGHT NOW!

We were joking around during HangOps on Nov 7 about setting up a website where people could get DevOps certified, much like were were all certified at DevOpsDays Belgium.   Just threw together a quick script to allow you to do just that.   Could obviously stick this on a website somewhere as a CGI.

## Requirements

You will need reportlab to generate the PDF.  

```bash
pip install -r requirements.txt
```


## Usage

```bash
./gendocert.py "Dave Mangot"
```
substitute your own username!   Should generate you a PDF suitable for printing.

Enjoy.

