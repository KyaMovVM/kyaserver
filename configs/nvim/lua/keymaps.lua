local map = vim.keymap.set

-- Nvim-tree
map("n", "<leader>e", "<cmd>NvimTreeToggle<cr>", { desc = "Открыть/закрыть дерево файлов" })
map("n", "<leader>f", "<cmd>NvimTreeFocus<cr>", { desc = "Фокус на дерево файлов" })

-- Навигация по окнам
map("n", "<C-h>", "<C-w>h", { desc = "Окно слева" })
map("n", "<C-j>", "<C-w>j", { desc = "Окно снизу" })
map("n", "<C-k>", "<C-w>k", { desc = "Окно сверху" })
map("n", "<C-l>", "<C-w>l", { desc = "Окно справа" })

-- Убрать подсветку поиска
map("n", "<Esc>", "<cmd>nohlsearch<cr>", { desc = "Убрать подсветку поиска" })

-- Перемещение строк в visual mode
map("v", "J", ":m '>+1<cr>gv=gv", { desc = "Сдвинуть строку вниз" })
map("v", "K", ":m '<-2<cr>gv=gv", { desc = "Сдвинуть строку вверх" })
