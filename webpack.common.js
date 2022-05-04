const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");
//const RemoveEmptyScriptsPlugin = require('webpack-remove-empty-scripts');
//const PurgecssPlugin = require('purgecss-webpack-plugin')
const glob = require('glob');
const path = require('path');

const isProduction = process.env.NODE_ENV !== 'production';


module.exports = {
    entry: {
        app: './hello_api/_app/app.js'
    },
    output: {
        path: path.resolve(__dirname, 'hello_api/_static/dist'),
        filename: '[name].js',
        chunkFilename: '[id].[chunkhash].js'
    },
    module: {
        rules: [
            {
                test: /.s?css$/,
                use: [MiniCssExtractPlugin.loader, "css-loader", "postcss-loader", "sass-loader"],
            },
            {
                test: /\.js$/,
                use: 'babel-loader',
            }
        ],
    },
    optimization: {
        minimizer: [
            // For webpack@5 you can use the `...` syntax to extend existing minimizers
            // (i.e. `terser-webpack-plugin`), uncomment the next line
            `...`,
             new CssMinimizerPlugin(),
        ],
    },
    plugins: [
      new MiniCssExtractPlugin(),
      //new PurgecssPlugin({
      //    paths: glob.sync(`./hello_api/_app/templates/**/*`,  { nodir: true }),
      //}),
    ],
};
