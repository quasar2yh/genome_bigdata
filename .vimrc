set history=10000
set autoread
set autoindent
set title
set laststatus=2
set paste
set hlsearch
set incsearch
set showmatch
set number
set cursorline
set cursorcolumn
set expandtab
set shiftwidth=4
set softtabstop=4
set tabstop=4
set background=dark
set t_Co=256
syntax enable
set mouse=a
au BufReadPost *
    \ if line("'\"")>0 && line("'\"") <= line("$") |
    \ exe "norm g'\"" |
    \ endif

