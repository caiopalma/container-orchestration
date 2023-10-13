FROM php:8.2-apache
RUN rm /etc/apt/preferences.d/no-debian-php \
    && apt-get update -y && apt-get install -y \
    libxml2-dev \
    php-soap \
    && docker-php-ext-install soap
WORKDIR /var/www/public_html