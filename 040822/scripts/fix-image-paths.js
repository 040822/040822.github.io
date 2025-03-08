console.log('js file loaded');
hexo.extend.filter.register('before_post_render', function(data) {
    //console.log('Original content:', data.content);
    // 替换形如 ![[name]] 的内容为 ![](name)
    data.content = data.content.replace(/!\[\[(.*?)\]\]/g, '![]($1)');
    // 打印替换后的内容
    //console.log('Modified content:', data.content);
    // 返回修改后的数据
    return data;
}, 1);