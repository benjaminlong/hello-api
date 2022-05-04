var path = require('path');
const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');


module.exports = merge(common, {
    mode: 'production',
    devtool: 'source-map',
    optimization: {
        minimize: true,
    },
    // plugins: [
    //   `...`,
    //   new MiniCssExtractPlugin(
    //     filename: "[name].min.css",
    //     chunkFilename: "[id].min.css",
    //   ),
    // ],
});
