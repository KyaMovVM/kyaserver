local opt = vim.opt

-- Номера строк
opt.number = true
opt.relativenumber = true

-- Отступы
opt.tabstop = 4
opt.shiftwidth = 4
opt.expandtab = true
opt.smartindent = true

-- Поиск
opt.ignorecase = true
opt.smartcase = true
opt.hlsearch = true
opt.incsearch = true

-- Внешний вид
opt.termguicolors = true
opt.signcolumn = "yes"
opt.cursorline = true
opt.scrolloff = 8

-- Поведение
opt.splitright = true
opt.splitbelow = true
opt.mouse = "a"
opt.clipboard = "unnamedplus"
opt.undofile = true
opt.swapfile = false
opt.updatetime = 250

-- Python provider
vim.g.python3_host_prog = "/usr/bin/python3"

-- Leader key
vim.g.mapleader = " "
vim.g.maplocalleader = " "
