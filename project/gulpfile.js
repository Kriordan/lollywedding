var gulp = require('gulp');
var browserSync = require('browser-sync').create();
var scss = require('gulp-sass');

gulp.task('serve', ['scss'], function() {

    browserSync.init({
        proxy: "localhost:5000"
    });

    gulp.watch("static/scss/*.scss", ['scss']);
    gulp.watch("templates/*.html").on("change", browserSync.reload);
});

gulp.task('scss', function() {
    return gulp.src('static/scss/main.scss')
        .pipe(scss().on('error', scss.logError))
        .pipe(gulp.dest('static/css'))
        .pipe(browserSync.stream());
});

gulp.task('default', ['serve']);
