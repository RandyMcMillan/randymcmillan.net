SHELL                                   := /bin/bash
PWD 									?= pwd_unknown
TIME 									:= $(shell date +%s)
export TIME

ifeq ($(project),)
PROJECT_NAME							:= $(notdir $(PWD))
else
PROJECT_NAME							:= $(project)
endif
export PROJECT_NAME

#GIT CONFIG
GIT_USER_NAME							:= $(shell git config user.name)
export GIT_USER_NAME
GH_USER_NAME							:= $(shell git config user.name)
#MIRRORS
GH_USER_REPO    						:= $(GH_USER_NAME).github.io
KB_USER_REPO   	        				:= $(GH_USER_NAME).keybase.pub
#GITHUB RUNNER CONFIGS
ifneq ($(ghuser),)
GH_USER_NAME := $(ghuser)
GH_USER_REPO := $(ghuser).github.io
endif
ifneq ($(kbuser),)
KB_USER_NAME := $(kbuser)
KB_USER_REPO := $(kbuser).keybase.pub
endif
export GIT_USER_NAME
export GH_USER_REPO
export KB_USER_REPO

GIT_USER_EMAIL							:= $(shell git config user.email)
export GIT_USER_EMAIL
GIT_SERVER								:= https://github.com
export GIT_SERVER
GIT_SSH_SERVER							:= git@github.com
export GIT_SSH_SERVER
GIT_PROFILE								:= $(shell git config user.name)
export GIT_PROFILE
GIT_BRANCH								:= $(shell git rev-parse --abbrev-ref HEAD)
export GIT_BRANCH
GIT_HASH								:= $(shell git rev-parse --short HEAD)
export GIT_HASH
GIT_PREVIOUS_HASH						:= $(shell git rev-parse --short master@{1})
export GIT_PREVIOUS_HASH
GIT_REPO_ORIGIN							:= $(shell git remote get-url origin)
export GIT_REPO_ORIGIN
GIT_REPO_NAME							:= $(PROJECT_NAME)
export GIT_REPO_NAME
GIT_REPO_PATH							:= $(HOME)/$(GIT_REPO_NAME)
export GIT_REPO_PATH

BASENAME := $(shell basename -s .git `git config --get remote.origin.url`)
export BASENAME

# Force the user to explicitly select public - public=true
# export KB_PUBLIC=public && make keybase-public
ifeq ($(public),true)
KB_PUBLIC  := public
else
KB_PUBLIC  := private
endif
export KB_PUBLIC

ifeq ($(libs),)
LIBS  := ./libs
else
LIBS  := $(libs)
endif
export LIBS

SPHINXOPTS            =
SPHINXBUILD           = sphinx-build
PAPER                 =
BUILDDIR              = _build
PRIVATE_BUILDDIR      = _private_build

# Internal variables.
PAPEROPT_a4           = -D latex_paper_size=a4
PAPEROPT_letter       = -D latex_paper_size=letter
ALLSPHINXOPTS         = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
PRIVATE_ALLSPHINXOPTS = -d $(PRIVATE_BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help
help: report
	@echo ""
	@echo "  make docs"
	@echo "  make push"
	@echo ""
	@echo ""

.PHONY: report
report: 
	@echo ''
	@echo '	[ARGUMENTS]	'
	@echo '      args:'
	@echo '        - TIME=${TIME}'
	@echo '        - PROJECT_NAME=${PROJECT_NAME}'
	@echo '        - GIT_USER_NAME=${GIT_USER_NAME}'
	@echo '        - GH_USER_REPO=${GH_USER_REPO}'
	@echo '        - KB_USER_REPO=${KB_USER_REPO}'
	@echo '        - GIT_USER_EMAIL=${GIT_USER_EMAIL}'
	@echo '        - GIT_SERVER=${GIT_SERVER}'
	@echo '        - GIT_PROFILE=${GIT_PROFILE}'
	@echo '        - GIT_BRANCH=${GIT_BRANCH}'
	@echo '        - GIT_HASH=${GIT_HASH}'
	@echo '        - GIT_PREVIOUS_HASH=${GIT_PREVIOUS_HASH}'
	@echo '        - GIT_REPO_ORIGIN=${GIT_REPO_ORIGIN}'
	@echo '        - GIT_REPO_NAME=${GIT_REPO_NAME}'
	@echo '        - GIT_REPO_PATH=${GIT_REPO_PATH}'

.PHONY: git-add
.ONESHELL:
git-add: remove
	@echo git-add

	git add --ignore-errors GNUmakefile
	git add --ignore-errors README.md
	git add --ignore-errors sources/*.md
	git add --ignore-errors sources/*.html
	git add --ignore-errors TIME
	git add --ignore-errors GLOBAL
	git add --ignore-errors CNAME
	git add --ignore-errors touch-block-time.py
	git add --ignore-errors *.py
	#git add --ignore-errors sources/*.py
	git add --ignore-errors index.html
	git add --ignore-errors .gitignore
	git add --ignore-errors .github
	git add --ignore-errors *.sh
	git add --ignore-errors *.yml

.PHONY: push
.ONESHELL:
push: remove git-add docs touch-time touch-block-time
	@echo push

	git commit -m 'make push by $(GIT_USER_NAME) on $(TIME)'
	git push origin	+master:master

.PHONY: branch
.ONESHELL:
branch: remove git-add docs touch-time touch-block-time
	@echo branch

	git add --ignore-errors GNUmakefile TIME GLOBAL .github *.sh *.yml
	git add --ignore-errors .github
	git commit -m 'make branch by $(GIT_USER_NAME) on $(TIME)'
	git branch $(TIME)
	git push --all

.PHONY: global-branch
.ONESHELL:
global-branch: remove git-add docs touch-time touch-global touch-block-time
	@echo global-branch
	bash -c "git add --ignore-errors * .github && \
		git commit -m 'make global-branch by $(GIT_USER_NAME) on global-$(TIME)'"
		git branch global-$(TIME)
		git push --all

.PHONY: time-branch
.ONESHELL:
time-branch: remove git-add docs touch-time touch-block-time
	@echo time-branch
	bash -c "git add --ignore-errors * .github && \
		git commit -m 'make time-branch by $(GIT_USER_NAME) on time-$(TIME)'"
		git branch time-$(TIME)
		git push --all

.PHONY: touch-time
.ONESHELL:
touch-time: remove git-add docs touch-block-time
	@echo touch-time
	echo $(TIME) $(shell git rev-parse HEAD) > TIME

.PHONY: touch-global
.ONESHELL:
touch-global: remove git-add docs touch-block-time
	@echo touch-global
	echo $(TIME) $(shell git rev-parse HEAD) > GLOBAL

.PHONY: touch-block-time
.ONESHELL:
touch-block-time: remove git-add docs
	@echo touch-block-time
	bash -c "pip install --user blockcypher"
	./touch-block-time.py

.PHONY: automate
automate: touch-time git-add
	@echo automate
	./.github/workflows/automate.sh

.PHONY: docs
docs: git-add awesome
	#@echo docs
	bash -c "if pgrep MacDown; then pkill MacDown; fi"
	#bash -c "curl https://raw.githubusercontent.com/sindresorhus/awesome/main/readme.md -o ./sources/AWESOME-temp.md"
	bash -c 'cat $(PWD)/sources/HEADER.md                >  $(PWD)/README.md'
	bash -c 'cat $(PWD)/sources/COMMANDS.md              >> $(PWD)/README.md'
	bash -c 'cat $(PWD)/sources/FOOTER.md                >> $(PWD)/README.md'
	brew install pandoc
	#bash -c 'pandoc -s README.md -o index.html  --metadata title="$(GH_USER_REPO)" '
	bash -c 'pandoc -s README.md -o index.html'
	bash -c "if hash open 2>/dev/null; then open README.md; fi || echo failed to open README.md"
	git add --ignore-errors sources/*.md
	git add --ignore-errors *.md
	#git ls-files -co --exclude-standard | grep '\.md/$\' | xargs git 

.PHONY: awesome
awesome:
	@echo awesome

	bash -c "brew install curl gnu-sed pandoc"

    bash -c "curl https://www.bitcoin.com/bitcoin.pdf -o bitcoin.pdf && rm -f bitcoin.pdf"

	bash -c "curl https://raw.githubusercontent.com/sindresorhus/awesome/main/readme.md -o ./sources/AWESOME-temp.md"
	bash -c "sed '1,136d' ~/randymcmillan/sources/AWESOME-temp.md > ./sources/AWESOME.md"
	bash -c "pandoc -s ~/randymcmillan/sources/AWESOME.md -o ./sources/awesome.html"

.PHONY: remove
remove:
	rm -rf dotfiles
	rm -rf legit

.PHONY: dotfiles
.ONESHELL:
dotfiles:
	@echo dotfiles

	if [ -f ~/dotfiles/README.md ]; then make -C dotfiles ; else git clone -b master --depth 1 https://github.com/randymcmillan/dotfiles ~/dotfiles; fi
	make all -C ~/dotfiles

.PHONY: legit
.ONESHELL:
legit:

	if [ -f ./legit/README.md ]; then make -C dotfiles ; else git clone -b master --depth 1 https://github.com/randymcmillan/legit ./legit; fi
	#TODO make all
	#make all -C legit
	cd legit && ./make-legit.sh
	
.PHONY: clean
.ONESHELL:
clean: touch-time touch-global
	bash -c "rm -rf $(BUILDDIR)"

.PHONY: serve
.ONESHELL:
serve:
	bash -c "python3 -m http.server 8000 -d . &"

.PHONY: failure
failure:
	@-/bin/false && ([ $$? -eq 0 ] && echo "success!") || echo "failure!"
.PHONY: success
success:
	@-/bin/true && ([ $$? -eq 0 ] && echo "success!") || echo "failure!"

