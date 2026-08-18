local has_imagemagick = vim.fn.executable("magick") == 1 or vim.fn.executable("convert") == 1

return {
    {
        "benlubas/molten-nvim",
        version = "^1.0.0",
        build = ":UpdateRemotePlugins",
        dependencies = has_imagemagick and { "3rd/image.nvim" } or {},
        init = function()
            vim.g.molten_output_win_max_height = 20
            vim.g.molten_auto_open_output = true
            vim.g.molten_wrap_output = true
            vim.g.molten_virt_text_output = true
            vim.g.molten_virt_lines_off_by_1 = true
            vim.g.molten_image_provider = has_imagemagick and "image.nvim" or "none"
        end,
        config = function()
            local map = vim.keymap.set
            map("n", "<leader>mi", "<cmd>MoltenInit python3<cr>", { desc = "Molten: запуск ядра Python" })
            map("n", "<leader>ml", "<cmd>MoltenEvaluateLine<cr>", { desc = "Molten: выполнить строку" })
            map("v", "<leader>m", ":<C-u>MoltenEvaluateVisual<cr>gv", { desc = "Molten: выполнить выделение" })
            map("n", "<leader>mr", "<cmd>MoltenReevaluateCell<cr>", { desc = "Molten: перезапустить ячейку" })
            map("n", "<leader>md", "<cmd>MoltenDelete<cr>", { desc = "Molten: удалить ячейку" })
            map("n", "<leader>mo", "<cmd>MoltenShowOutput<cr>", { desc = "Molten: показать вывод" })
            map("n", "<leader>mh", "<cmd>MoltenHideOutput<cr>", { desc = "Molten: скрыть вывод" })
        end,
    },
    {
        "3rd/image.nvim",
        enabled = has_imagemagick,
        opts = {
            backend = "kitty",
            max_width = 100,
            max_height = 12,
            max_height_window_percentage = 50,
            integrations = {
                markdown = { enabled = true },
            },
        },
    },
}
