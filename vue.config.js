const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  transpileDependencies: ['vuetify'],
  devServer: {
    proxy: {
      '^/api': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
        pathRewrite: {
          '^/api': '',
        },
      },
    },
  },
  chainWebpack: (config) => {
    config.module
      .rule('pdf')
      .test(/\.pdf$/)
      .use('file-loader')
      .loader('file-loader')
      .options({
        name: '[name].[ext]',
      });
  },
});
