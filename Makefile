docker:
	docker build -t jek:latest --build-arg gems=$(shell python3 _get_gems.py) .

build:
	docker run --rm   --volume="$(CURDIR):/srv/jekyll"   -it jek:latest   jekyll build

serve:
	docker run --rm   --volume="$(CURDIR):/srv/jekyll"  -p 4000:4000  -it jek:latest   jekyll serve
