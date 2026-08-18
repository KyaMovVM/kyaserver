return {
    "nvim-tree/nvim-tree.lua",
    dependencies = {
        "nvim-tree/nvim-web-devicons",
    },
    config = function()
        -- Отключаем netrw (встроенный файловый менеджер)
        vim.g.loaded_netrw = 1
        vim.g.loaded_netrwPlugin = 1

        require("nvim-tree").setup({
            view = {
                width = 30,
                side = "left",
            },
            renderer = {
                group_empty = true,
                icons = {
                    show = {
                        file = true,
                        folder = true,
                        folder_arrow = true,
                        git = true,
                    },
                },
                indent_markers = {
                    enable = true,
                },
            },
            filters = {
                dotfiles = false,
                custom = { "^%.git$" },
            },
            git = {
                enable = true,
                ignore = false,
                show_on_dirs = true,
            },
            filesystem_watchers = {
                enable = true,
                debounce_delay = 50,
            },
            actions = {
                open_file = {
                    quit_on_open = false,
                    resize_window = true,
                },
            },
        })
    end,
}
