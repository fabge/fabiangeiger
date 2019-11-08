Title: Tailwind CSS, Pelican and Amazon S3
Date: 2019-11-08

## The early days

It has been some time since I've had a personal site.  
The way the site was set up, updated and deployed also has a multi-layered and wide-varied history.

In the early days, where I barely had a clue what I was doing, I used drag-and-drop (later FTP) to upload my files to a provider like HostGator.  
After getting more familier with web development my deployment shifted to a virtual machine, requests to my personal site were handled by NGINX.  
If you look closely, my hosting went from being kind of serverless to a fully self-hosted solution, bundled with all its pros and cons. Eventhough self-hosting gave me much more flexibility on the way I wanted to structure things, I was not satisfied with the solution. The virtual machine I rented was 5$/month and about as powerful as an older Raspberry Pi. If there had ever been more serious traffic, I'm not sure if the server had handled it, even if it was only static files.

## Back to serverless

Fast forward to today:  
My current favorite setup of hosting static sites is Amazon's S3 Bucket. Similarly to HostGator, you can upload your files to an S3 Bucket, configure it and voilà, your site is online. No installing of NGINX (or Docker and then an running an NGINX container) or other sorts of server management stuff necessary.

With the AWS Certificate Manager you can even provision `https` certificates and automatically renew them. CloudFront pushes your site to dozens of nodes around the world.

The first time I read about this way of deploying a static site was through Brandur Leach's article "[The Intrinsic Static Site](https://brandur.org/aws-intrinsic-static)". He sums it up with following features:

* Approximately unlimited scalability.
* As close to an operations-free experience as you’re ever likely to find.
* Full HTTPS support with a certificate that’s renewed automatically.
* A CDN with dozens of edge locations around the globe so that it’ll load quickly from anywhere.
* A GitHub-based workflow which will make publishing new content as easy as merging a pull request.

## Toolbox

I have combined three tools to make updates and the deployment of my personal site as easy and hassle-free as possible.

**Tailwind CSS**  
I really like working with Tailwind CSS to design my personal site. It doesn't restrict and standardise your design as much as Bootstrap does but still is contrained and opionated enough. It allows me to structure my site wihtout having to define arbitrary pixel widths or color schemes and makes me write way less code by doing so.

**Pelican**  
Writing articles or uploading photos should not have to be accompanied by having to write custom HTML to implement them into your site. Pelican is a Python-based static site generator, which allows me to write articles in Markdown and upload photos as they are. When I generate the site, the articles get compilied to HTML and embedded into the site. The photos are scaled and resized and embedded into the site as well.

**Amazon S3**  
The already mentioned Amazon S3 (Simple Storage Service) is an object storage service with a well documented API that allows a simple, yet highly scalable site hosting.

## Workflow

I manage my static site in Github. My project structure looks as follow:
```
.
├── Makefile
├── content
│   ├── images
│   └── posts
├── output
├── pelicanconf.py
├── plugins
│   ├── gallery
│   ├── ipynb
│   └── photos
├── tasks.py
└── theme
```

When I now want to write a new article or upload a new photo, my workflow is quite simple:  

1. Create a new `.md` article in my local `content/posts` directory or copy a photo to `content/images`.
2. Use Pelican to generate `.html` files from the written content (= execute `pelican content` in the terminal).
3. Push the changes to my Github repository.

I use Github Actions to continue the deployment process:  
After the changes are uploaded, a `actions/checkout@master` hook initiates the upload process to my S3 bucket.  
From there a combination of S3, Certificate Manager and CloudFront serve the HTTPS site to over 200 locations all over the world.

<!-- In the early days, where I barely had a clue what I was doing, I googled how to put a site on the internet
and stumbled upon HostGator. This service allowed me to upload my `.html` files and serve them straight from a folderstructure-like environment.  
In those early days, it offered a good way of providing the internet acces to your personal site, including all the `.css` and `.js` files needed.  
Euphoric and savvy as I (thought I) was, I thought this is all I will ever need and promptly purchased a 2-year subscription to save on the average monthly price.

Fast forward a couple of months, I got more and more into web development and wanted to try out a few things.

# Learning more about web development

The reason I got interested in how other projects were deployed was because I planned to make a product which was more than just a static site. I needed an environment which allowed me to run Python code and serve HTML at the same time.  
Equipped with the knowledge about webservers web-frameworks I  -->