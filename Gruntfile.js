module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
      },
      build: {
        src: 'core/static/js/base.js',
        dest: 'core/static/js/base.min.js'
      }
    },
    concat: {
      options: {
        separator: ';',
        stripBanners: true,
      },
      dist: {
        src: [
          'core/static/js/base.min.js', 
          'core/static/js/lib/jquery-2.1.1.min.js',
          'core/static/js/lib/bootstrap-3.1.1.min.js',
        ],
        dest: 'core/static/account.js',
      },
    },
  });

  // Load tasks
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-concat');

  // Default task(s).
  grunt.registerTask('default', ['uglify']);

};
