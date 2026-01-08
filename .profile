pathmunge() {
    case ":${PATH}:" in
        *:"$1":*)
            ;;
        *)
            if [ "$2" = "after" ] ; then
                PATH=$PATH:$1
            else
                PATH=$1:$PATH
            fi
    esac
}

# old zsh doesn't support [[ `cmd` ]] expr
which systemctl &> /dev/null
[[ $? -eq 0 ]] && systemctl --user import-environment PATH

export MAKEFLAGS=-j4
export PAGER='less -FXMr'
pathmunge ~/.local/bin
pathmunge ~/.bin

which nvim &> /dev/null
if [[ $? -eq 0 ]]; then
	EDITOR=nvim
	alias vi=nvim
	alias vim=nvim
else
	EDITOR=vim
fi
export EDITOR

[[ -f ~/.profile.extra ]] && . ~/.profile.extra

# for ccache
pathmunge /usr/lib64/ccache/bin/:/usr/lib/ccache/bin/
export CCACHE_DIR=/tmp/.ccache
