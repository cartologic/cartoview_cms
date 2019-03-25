# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-25 09:12
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cartoview_cms', '0049_auto_20190325_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(classname=b'full')), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock()), (b'header', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'header', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'h1', b'H1'), (b'h2', b'H2'), (b'h3', b'H3'), (b'h4', b'H4'), (b'h5', b'H5'), (b'h6', b'H6')], label=b'Header Size')), (b'text', wagtail.wagtailcore.blocks.CharBlock(label=b'Text', max_length=50))]), icon=b'title', template=b'cartoview_cms/streamfields/header.html')), (b'text_field', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(label=b'Text Field'))]), icon=b'fa-text-width', template=b'cartoview_cms/streamfields/text_field.html')), (b'list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(), label=b'Items'))]), icon=b'list-ul', template=b'cartoview_cms/streamfields/list.html')), (b'accordions', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(label=b'Title', max_length=50)), (b'content', wagtail.wagtailcore.blocks.RichTextBlock(label=b'Content'))]), icon=b'list-ol', template=b'cartoview_cms/streamfields/accordion.html')), (b'horizontal_tabs', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'icon', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'address-book', b'address-book'), (b'address-book-o', b'address-book-o'), (b'address-card', b'address-card'), (b'address-card-o', b'address-card-o'), (b'adjust', b'adjust'), (b'american-sign-language-interpreting', b'american-sign-language-interpreting'), (b'anchor', b'anchor'), (b'archive', b'archive'), (b'area-chart', b'area-chart'), (b'arrows', b'arrows'), (b'arrows-h', b'arrows-h'), (b'arrows-v', b'arrows-v'), (b'asl-interpreting ', b'asl-interpreting '), (b'assistive-listening-systems', b'assistive-listening-systems'), (b'asterisk', b'asterisk'), (b'at', b'at'), (b'audio-description', b'audio-description'), (b'automobile ', b'automobile '), (b'balance-scale', b'balance-scale'), (b'ban', b'ban'), (b'bank ', b'bank '), (b'bar-chart', b'bar-chart'), (b'bar-chart-o ', b'bar-chart-o '), (b'barcode', b'barcode'), (b'bars', b'bars'), (b'bath', b'bath'), (b'bathtub ', b'bathtub '), (b'battery ', b'battery '), (b'battery-0 ', b'battery-0 '), (b'battery-1 ', b'battery-1 '), (b'battery-2 ', b'battery-2 '), (b'battery-3 ', b'battery-3 '), (b'battery-4 ', b'battery-4 '), (b'battery-empty', b'battery-empty'), (b'battery-full', b'battery-full'), (b'battery-half', b'battery-half'), (b'battery-quarter', b'battery-quarter'), (b'battery-three-quarters', b'battery-three-quarters'), (b'bed', b'bed'), (b'beer', b'beer'), (b'bell', b'bell'), (b'bell-o', b'bell-o'), (b'bell-slash', b'bell-slash'), (b'bell-slash-o', b'bell-slash-o'), (b'bicycle', b'bicycle'), (b'binoculars', b'binoculars'), (b'birthday-cake', b'birthday-cake'), (b'blind', b'blind'), (b'bluetooth', b'bluetooth'), (b'bluetooth-b', b'bluetooth-b'), (b'bolt', b'bolt'), (b'bomb', b'bomb'), (b'book', b'book'), (b'bookmark', b'bookmark'), (b'bookmark-o', b'bookmark-o'), (b'braille', b'braille'), (b'briefcase', b'briefcase'), (b'bug', b'bug'), (b'building', b'building'), (b'building-o', b'building-o'), (b'bullhorn', b'bullhorn'), (b'bullseye', b'bullseye'), (b'bus', b'bus'), (b'cab ', b'cab '), (b'calculator', b'calculator'), (b'calendar', b'calendar'), (b'calendar-check-o', b'calendar-check-o'), (b'calendar-minus-o', b'calendar-minus-o'), (b'calendar-o', b'calendar-o'), (b'calendar-plus-o', b'calendar-plus-o'), (b'calendar-times-o', b'calendar-times-o'), (b'camera', b'camera'), (b'camera-retro', b'camera-retro'), (b'car', b'car'), (b'caret-square-o-down', b'caret-square-o-down'), (b'caret-square-o-left', b'caret-square-o-left'), (b'caret-square-o-right', b'caret-square-o-right'), (b'caret-square-o-up', b'caret-square-o-up'), (b'cart-arrow-down', b'cart-arrow-down'), (b'cart-plus', b'cart-plus'), (b'cc', b'cc'), (b'certificate', b'certificate'), (b'check', b'check'), (b'check-circle', b'check-circle'), (b'check-circle-o', b'check-circle-o'), (b'check-square', b'check-square'), (b'check-square-o', b'check-square-o'), (b'child', b'child'), (b'circle', b'circle'), (b'circle-o', b'circle-o'), (b'circle-o-notch', b'circle-o-notch'), (b'circle-thin', b'circle-thin'), (b'clock-o', b'clock-o'), (b'clone', b'clone'), (b'close ', b'close '), (b'cloud', b'cloud'), (b'cloud-download', b'cloud-download'), (b'cloud-upload', b'cloud-upload'), (b'code', b'code'), (b'code-fork', b'code-fork'), (b'coffee', b'coffee'), (b'cog', b'cog'), (b'cogs', b'cogs'), (b'comment', b'comment'), (b'comment-o', b'comment-o'), (b'commenting', b'commenting'), (b'commenting-o', b'commenting-o'), (b'comments', b'comments'), (b'comments-o', b'comments-o'), (b'compass', b'compass'), (b'copyright', b'copyright'), (b'creative-commons', b'creative-commons'), (b'credit-card', b'credit-card'), (b'credit-card-alt', b'credit-card-alt'), (b'crop', b'crop'), (b'crosshairs', b'crosshairs'), (b'cube', b'cube'), (b'cubes', b'cubes'), (b'cutlery', b'cutlery'), (b'dashboard ', b'dashboard '), (b'database', b'database'), (b'deaf', b'deaf'), (b'deafness ', b'deafness '), (b'desktop', b'desktop'), (b'diamond', b'diamond'), (b'dot-circle-o', b'dot-circle-o'), (b'download', b'download'), (b'drivers-license ', b'drivers-license '), (b'drivers-license-o ', b'drivers-license-o '), (b'edit ', b'edit '), (b'ellipsis-h', b'ellipsis-h'), (b'ellipsis-v', b'ellipsis-v'), (b'envelope', b'envelope'), (b'envelope-o', b'envelope-o'), (b'envelope-open', b'envelope-open'), (b'envelope-open-o', b'envelope-open-o'), (b'envelope-square', b'envelope-square'), (b'eraser', b'eraser'), (b'exchange', b'exchange'), (b'exclamation', b'exclamation'), (b'exclamation-circle', b'exclamation-circle'), (b'exclamation-triangle', b'exclamation-triangle'), (b'external-link', b'external-link'), (b'external-link-square', b'external-link-square'), (b'eye', b'eye'), (b'eye-slash', b'eye-slash'), (b'eyedropper', b'eyedropper'), (b'fax', b'fax'), (b'feed ', b'feed '), (b'female', b'female'), (b'fighter-jet', b'fighter-jet'), (b'file-archive-o', b'file-archive-o'), (b'file-audio-o', b'file-audio-o'), (b'file-code-o', b'file-code-o'), (b'file-excel-o', b'file-excel-o'), (b'file-image-o', b'file-image-o'), (b'file-movie-o ', b'file-movie-o '), (b'file-pdf-o', b'file-pdf-o'), (b'file-photo-o ', b'file-photo-o '), (b'file-picture-o ', b'file-picture-o '), (b'file-powerpoint-o', b'file-powerpoint-o'), (b'file-sound-o ', b'file-sound-o '), (b'file-video-o', b'file-video-o'), (b'file-word-o', b'file-word-o'), (b'file-zip-o ', b'file-zip-o '), (b'film', b'film'), (b'filter', b'filter'), (b'fire', b'fire'), (b'fire-extinguisher', b'fire-extinguisher'), (b'flag', b'flag'), (b'flag-checkered', b'flag-checkered'), (b'flag-o', b'flag-o'), (b'flash ', b'flash '), (b'flask', b'flask'), (b'folder', b'folder'), (b'folder-o', b'folder-o'), (b'folder-open', b'folder-open'), (b'folder-open-o', b'folder-open-o'), (b'frown-o', b'frown-o'), (b'futbol-o', b'futbol-o'), (b'gamepad', b'gamepad'), (b'gavel', b'gavel'), (b'gear ', b'gear '), (b'gears ', b'gears '), (b'gift', b'gift'), (b'glass', b'glass'), (b'globe', b'globe'), (b'graduation-cap', b'graduation-cap'), (b'group ', b'group '), (b'hand-grab-o ', b'hand-grab-o '), (b'hand-lizard-o', b'hand-lizard-o'), (b'hand-paper-o', b'hand-paper-o'), (b'hand-peace-o', b'hand-peace-o'), (b'hand-pointer-o', b'hand-pointer-o'), (b'hand-rock-o', b'hand-rock-o'), (b'hand-scissors-o', b'hand-scissors-o'), (b'hand-spock-o', b'hand-spock-o'), (b'hand-stop-o ', b'hand-stop-o '), (b'handshake-o', b'handshake-o'), (b'hard-of-hearing ', b'hard-of-hearing '), (b'hashtag', b'hashtag'), (b'hdd-o', b'hdd-o'), (b'headphones', b'headphones'), (b'heart', b'heart'), (b'heart-o', b'heart-o'), (b'heartbeat', b'heartbeat'), (b'history', b'history'), (b'home', b'home'), (b'hotel ', b'hotel '), (b'hourglass', b'hourglass'), (b'hourglass-1 ', b'hourglass-1 '), (b'hourglass-2 ', b'hourglass-2 '), (b'hourglass-3 ', b'hourglass-3 '), (b'hourglass-end', b'hourglass-end'), (b'hourglass-half', b'hourglass-half'), (b'hourglass-o', b'hourglass-o'), (b'hourglass-start', b'hourglass-start'), (b'i-cursor', b'i-cursor'), (b'id-badge', b'id-badge'), (b'id-card', b'id-card'), (b'id-card-o', b'id-card-o'), (b'image ', b'image '), (b'inbox', b'inbox'), (b'industry', b'industry'), (b'info', b'info'), (b'info-circle', b'info-circle'), (b'institution ', b'institution '), (b'key', b'key'), (b'keyboard-o', b'keyboard-o'), (b'language', b'language'), (b'laptop', b'laptop'), (b'leaf', b'leaf'), (b'legal ', b'legal '), (b'lemon-o', b'lemon-o'), (b'level-down', b'level-down'), (b'level-up', b'level-up'), (b'life-bouy ', b'life-bouy '), (b'life-buoy ', b'life-buoy '), (b'life-ring', b'life-ring'), (b'life-saver ', b'life-saver '), (b'lightbulb-o', b'lightbulb-o'), (b'line-chart', b'line-chart'), (b'location-arrow', b'location-arrow'), (b'lock', b'lock'), (b'low-vision', b'low-vision'), (b'magic', b'magic'), (b'magnet', b'magnet'), (b'mail-forward ', b'mail-forward '), (b'mail-reply ', b'mail-reply '), (b'mail-reply-all ', b'mail-reply-all '), (b'male', b'male'), (b'map', b'map'), (b'map-marker', b'map-marker'), (b'map-o', b'map-o'), (b'map-pin', b'map-pin'), (b'map-signs', b'map-signs'), (b'meh-o', b'meh-o'), (b'microchip', b'microchip'), (b'microphone', b'microphone'), (b'microphone-slash', b'microphone-slash'), (b'minus', b'minus'), (b'minus-circle', b'minus-circle'), (b'minus-square', b'minus-square'), (b'minus-square-o', b'minus-square-o'), (b'mobile', b'mobile'), (b'mobile-phone ', b'mobile-phone '), (b'money', b'money'), (b'moon-o', b'moon-o'), (b'mortar-board ', b'mortar-board '), (b'motorcycle', b'motorcycle'), (b'mouse-pointer', b'mouse-pointer'), (b'music', b'music'), (b'navicon ', b'navicon '), (b'newspaper-o', b'newspaper-o'), (b'object-group', b'object-group'), (b'object-ungroup', b'object-ungroup'), (b'paint-brush', b'paint-brush'), (b'paper-plane', b'paper-plane'), (b'paper-plane-o', b'paper-plane-o'), (b'paw', b'paw'), (b'pencil', b'pencil'), (b'pencil-square', b'pencil-square'), (b'pencil-square-o', b'pencil-square-o'), (b'percent', b'percent'), (b'phone', b'phone'), (b'phone-square', b'phone-square'), (b'photo ', b'photo '), (b'picture-o', b'picture-o'), (b'pie-chart', b'pie-chart'), (b'plane', b'plane'), (b'plug', b'plug'), (b'plus', b'plus'), (b'plus-circle', b'plus-circle'), (b'plus-square', b'plus-square'), (b'plus-square-o', b'plus-square-o'), (b'podcast', b'podcast'), (b'power-off', b'power-off'), (b'print', b'print'), (b'puzzle-piece', b'puzzle-piece'), (b'qrcode', b'qrcode'), (b'question', b'question'), (b'question-circle', b'question-circle'), (b'question-circle-o', b'question-circle-o'), (b'quote-left', b'quote-left'), (b'quote-right', b'quote-right'), (b'random', b'random'), (b'recycle', b'recycle'), (b'refresh', b'refresh'), (b'registered', b'registered'), (b'remove ', b'remove '), (b'reorder ', b'reorder '), (b'reply', b'reply'), (b'reply-all', b'reply-all'), (b'retweet', b'retweet'), (b'road', b'road'), (b'rocket', b'rocket'), (b'rss', b'rss'), (b'rss-square', b'rss-square'), (b's15 ', b's15 '), (b'search', b'search'), (b'search-minus', b'search-minus'), (b'search-plus', b'search-plus'), (b'send ', b'send '), (b'send-o ', b'send-o '), (b'server', b'server'), (b'share', b'share'), (b'share-alt', b'share-alt'), (b'share-alt-square', b'share-alt-square'), (b'share-square', b'share-square'), (b'share-square-o', b'share-square-o'), (b'shield', b'shield'), (b'ship', b'ship'), (b'shopping-bag', b'shopping-bag'), (b'shopping-basket', b'shopping-basket'), (b'shopping-cart', b'shopping-cart'), (b'shower', b'shower'), (b'sign-in', b'sign-in'), (b'sign-language', b'sign-language'), (b'sign-out', b'sign-out'), (b'signal', b'signal'), (b'signing ', b'signing '), (b'sitemap', b'sitemap'), (b'sliders', b'sliders'), (b'smile-o', b'smile-o'), (b'snowflake-o', b'snowflake-o'), (b'soccer-ball-o ', b'soccer-ball-o '), (b'sort', b'sort'), (b'sort-alpha-asc', b'sort-alpha-asc'), (b'sort-alpha-desc', b'sort-alpha-desc'), (b'sort-amount-asc', b'sort-amount-asc'), (b'sort-amount-desc', b'sort-amount-desc'), (b'sort-asc', b'sort-asc'), (b'sort-desc', b'sort-desc'), (b'sort-down ', b'sort-down '), (b'sort-numeric-asc', b'sort-numeric-asc'), (b'sort-numeric-desc', b'sort-numeric-desc'), (b'sort-up ', b'sort-up '), (b'space-shuttle', b'space-shuttle'), (b'spinner', b'spinner'), (b'spoon', b'spoon'), (b'square', b'square'), (b'square-o', b'square-o'), (b'star', b'star'), (b'star-half', b'star-half'), (b'star-half-empty ', b'star-half-empty '), (b'star-half-full ', b'star-half-full '), (b'star-half-o', b'star-half-o'), (b'star-o', b'star-o'), (b'sticky-note', b'sticky-note'), (b'sticky-note-o', b'sticky-note-o'), (b'street-view', b'street-view'), (b'suitcase', b'suitcase'), (b'sun-o', b'sun-o'), (b'support ', b'support '), (b'tablet', b'tablet'), (b'tachometer', b'tachometer'), (b'tag', b'tag'), (b'tags', b'tags'), (b'tasks', b'tasks'), (b'taxi', b'taxi'), (b'television', b'television'), (b'terminal', b'terminal'), (b'thermometer ', b'thermometer '), (b'thermometer-0 ', b'thermometer-0 '), (b'thermometer-1 ', b'thermometer-1 '), (b'thermometer-2 ', b'thermometer-2 '), (b'thermometer-3 ', b'thermometer-3 '), (b'thermometer-4 ', b'thermometer-4 '), (b'thermometer-empty', b'thermometer-empty'), (b'thermometer-full', b'thermometer-full'), (b'thermometer-half', b'thermometer-half'), (b'thermometer-quarter', b'thermometer-quarter'), (b'thermometer-three-quarters', b'thermometer-three-quarters'), (b'thumb-tack', b'thumb-tack'), (b'thumbs-down', b'thumbs-down'), (b'thumbs-o-down', b'thumbs-o-down'), (b'thumbs-o-up', b'thumbs-o-up'), (b'thumbs-up', b'thumbs-up'), (b'ticket', b'ticket'), (b'times', b'times'), (b'times-circle', b'times-circle'), (b'times-circle-o', b'times-circle-o'), (b'times-rectangle ', b'times-rectangle '), (b'times-rectangle-o ', b'times-rectangle-o '), (b'tint', b'tint'), (b'toggle-down ', b'toggle-down '), (b'toggle-left ', b'toggle-left '), (b'toggle-off', b'toggle-off'), (b'toggle-on', b'toggle-on'), (b'toggle-right ', b'toggle-right '), (b'toggle-up ', b'toggle-up '), (b'trademark', b'trademark'), (b'trash', b'trash'), (b'trash-o', b'trash-o'), (b'tree', b'tree'), (b'trophy', b'trophy'), (b'truck', b'truck'), (b'tty', b'tty'), (b'tv ', b'tv '), (b'umbrella', b'umbrella'), (b'universal-access', b'universal-access'), (b'university', b'university'), (b'unlock', b'unlock'), (b'unlock-alt', b'unlock-alt'), (b'unsorted ', b'unsorted '), (b'upload', b'upload'), (b'user', b'user'), (b'user-circle', b'user-circle'), (b'user-circle-o', b'user-circle-o'), (b'user-o', b'user-o'), (b'user-plus', b'user-plus'), (b'user-secret', b'user-secret'), (b'user-times', b'user-times'), (b'users', b'users'), (b'vcard ', b'vcard '), (b'vcard-o ', b'vcard-o '), (b'video-camera', b'video-camera'), (b'volume-control-phone', b'volume-control-phone'), (b'volume-down', b'volume-down'), (b'volume-off', b'volume-off'), (b'volume-up', b'volume-up'), (b'warning ', b'warning '), (b'wheelchair', b'wheelchair'), (b'wheelchair-alt', b'wheelchair-alt'), (b'wifi', b'wifi'), (b'window-close', b'window-close'), (b'window-close-o', b'window-close-o'), (b'window-maximize', b'window-maximize'), (b'window-minimize', b'window-minimize'), (b'window-restore', b'window-restore'), (b'wrench', b'wrench')], label=b'Icon', required=False)), (b'title', wagtail.wagtailcore.blocks.CharBlock(label=b'Title', max_length=50)), (b'content', wagtail.wagtailcore.blocks.RichTextBlock(label=b'Content'))]), icon=b'list-ol', template=b'cartoview_cms/streamfields/horizontal_tab.html')), (b'verticale_tabs', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'icon', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'address-book', b'address-book'), (b'address-book-o', b'address-book-o'), (b'address-card', b'address-card'), (b'address-card-o', b'address-card-o'), (b'adjust', b'adjust'), (b'american-sign-language-interpreting', b'american-sign-language-interpreting'), (b'anchor', b'anchor'), (b'archive', b'archive'), (b'area-chart', b'area-chart'), (b'arrows', b'arrows'), (b'arrows-h', b'arrows-h'), (b'arrows-v', b'arrows-v'), (b'asl-interpreting ', b'asl-interpreting '), (b'assistive-listening-systems', b'assistive-listening-systems'), (b'asterisk', b'asterisk'), (b'at', b'at'), (b'audio-description', b'audio-description'), (b'automobile ', b'automobile '), (b'balance-scale', b'balance-scale'), (b'ban', b'ban'), (b'bank ', b'bank '), (b'bar-chart', b'bar-chart'), (b'bar-chart-o ', b'bar-chart-o '), (b'barcode', b'barcode'), (b'bars', b'bars'), (b'bath', b'bath'), (b'bathtub ', b'bathtub '), (b'battery ', b'battery '), (b'battery-0 ', b'battery-0 '), (b'battery-1 ', b'battery-1 '), (b'battery-2 ', b'battery-2 '), (b'battery-3 ', b'battery-3 '), (b'battery-4 ', b'battery-4 '), (b'battery-empty', b'battery-empty'), (b'battery-full', b'battery-full'), (b'battery-half', b'battery-half'), (b'battery-quarter', b'battery-quarter'), (b'battery-three-quarters', b'battery-three-quarters'), (b'bed', b'bed'), (b'beer', b'beer'), (b'bell', b'bell'), (b'bell-o', b'bell-o'), (b'bell-slash', b'bell-slash'), (b'bell-slash-o', b'bell-slash-o'), (b'bicycle', b'bicycle'), (b'binoculars', b'binoculars'), (b'birthday-cake', b'birthday-cake'), (b'blind', b'blind'), (b'bluetooth', b'bluetooth'), (b'bluetooth-b', b'bluetooth-b'), (b'bolt', b'bolt'), (b'bomb', b'bomb'), (b'book', b'book'), (b'bookmark', b'bookmark'), (b'bookmark-o', b'bookmark-o'), (b'braille', b'braille'), (b'briefcase', b'briefcase'), (b'bug', b'bug'), (b'building', b'building'), (b'building-o', b'building-o'), (b'bullhorn', b'bullhorn'), (b'bullseye', b'bullseye'), (b'bus', b'bus'), (b'cab ', b'cab '), (b'calculator', b'calculator'), (b'calendar', b'calendar'), (b'calendar-check-o', b'calendar-check-o'), (b'calendar-minus-o', b'calendar-minus-o'), (b'calendar-o', b'calendar-o'), (b'calendar-plus-o', b'calendar-plus-o'), (b'calendar-times-o', b'calendar-times-o'), (b'camera', b'camera'), (b'camera-retro', b'camera-retro'), (b'car', b'car'), (b'caret-square-o-down', b'caret-square-o-down'), (b'caret-square-o-left', b'caret-square-o-left'), (b'caret-square-o-right', b'caret-square-o-right'), (b'caret-square-o-up', b'caret-square-o-up'), (b'cart-arrow-down', b'cart-arrow-down'), (b'cart-plus', b'cart-plus'), (b'cc', b'cc'), (b'certificate', b'certificate'), (b'check', b'check'), (b'check-circle', b'check-circle'), (b'check-circle-o', b'check-circle-o'), (b'check-square', b'check-square'), (b'check-square-o', b'check-square-o'), (b'child', b'child'), (b'circle', b'circle'), (b'circle-o', b'circle-o'), (b'circle-o-notch', b'circle-o-notch'), (b'circle-thin', b'circle-thin'), (b'clock-o', b'clock-o'), (b'clone', b'clone'), (b'close ', b'close '), (b'cloud', b'cloud'), (b'cloud-download', b'cloud-download'), (b'cloud-upload', b'cloud-upload'), (b'code', b'code'), (b'code-fork', b'code-fork'), (b'coffee', b'coffee'), (b'cog', b'cog'), (b'cogs', b'cogs'), (b'comment', b'comment'), (b'comment-o', b'comment-o'), (b'commenting', b'commenting'), (b'commenting-o', b'commenting-o'), (b'comments', b'comments'), (b'comments-o', b'comments-o'), (b'compass', b'compass'), (b'copyright', b'copyright'), (b'creative-commons', b'creative-commons'), (b'credit-card', b'credit-card'), (b'credit-card-alt', b'credit-card-alt'), (b'crop', b'crop'), (b'crosshairs', b'crosshairs'), (b'cube', b'cube'), (b'cubes', b'cubes'), (b'cutlery', b'cutlery'), (b'dashboard ', b'dashboard '), (b'database', b'database'), (b'deaf', b'deaf'), (b'deafness ', b'deafness '), (b'desktop', b'desktop'), (b'diamond', b'diamond'), (b'dot-circle-o', b'dot-circle-o'), (b'download', b'download'), (b'drivers-license ', b'drivers-license '), (b'drivers-license-o ', b'drivers-license-o '), (b'edit ', b'edit '), (b'ellipsis-h', b'ellipsis-h'), (b'ellipsis-v', b'ellipsis-v'), (b'envelope', b'envelope'), (b'envelope-o', b'envelope-o'), (b'envelope-open', b'envelope-open'), (b'envelope-open-o', b'envelope-open-o'), (b'envelope-square', b'envelope-square'), (b'eraser', b'eraser'), (b'exchange', b'exchange'), (b'exclamation', b'exclamation'), (b'exclamation-circle', b'exclamation-circle'), (b'exclamation-triangle', b'exclamation-triangle'), (b'external-link', b'external-link'), (b'external-link-square', b'external-link-square'), (b'eye', b'eye'), (b'eye-slash', b'eye-slash'), (b'eyedropper', b'eyedropper'), (b'fax', b'fax'), (b'feed ', b'feed '), (b'female', b'female'), (b'fighter-jet', b'fighter-jet'), (b'file-archive-o', b'file-archive-o'), (b'file-audio-o', b'file-audio-o'), (b'file-code-o', b'file-code-o'), (b'file-excel-o', b'file-excel-o'), (b'file-image-o', b'file-image-o'), (b'file-movie-o ', b'file-movie-o '), (b'file-pdf-o', b'file-pdf-o'), (b'file-photo-o ', b'file-photo-o '), (b'file-picture-o ', b'file-picture-o '), (b'file-powerpoint-o', b'file-powerpoint-o'), (b'file-sound-o ', b'file-sound-o '), (b'file-video-o', b'file-video-o'), (b'file-word-o', b'file-word-o'), (b'file-zip-o ', b'file-zip-o '), (b'film', b'film'), (b'filter', b'filter'), (b'fire', b'fire'), (b'fire-extinguisher', b'fire-extinguisher'), (b'flag', b'flag'), (b'flag-checkered', b'flag-checkered'), (b'flag-o', b'flag-o'), (b'flash ', b'flash '), (b'flask', b'flask'), (b'folder', b'folder'), (b'folder-o', b'folder-o'), (b'folder-open', b'folder-open'), (b'folder-open-o', b'folder-open-o'), (b'frown-o', b'frown-o'), (b'futbol-o', b'futbol-o'), (b'gamepad', b'gamepad'), (b'gavel', b'gavel'), (b'gear ', b'gear '), (b'gears ', b'gears '), (b'gift', b'gift'), (b'glass', b'glass'), (b'globe', b'globe'), (b'graduation-cap', b'graduation-cap'), (b'group ', b'group '), (b'hand-grab-o ', b'hand-grab-o '), (b'hand-lizard-o', b'hand-lizard-o'), (b'hand-paper-o', b'hand-paper-o'), (b'hand-peace-o', b'hand-peace-o'), (b'hand-pointer-o', b'hand-pointer-o'), (b'hand-rock-o', b'hand-rock-o'), (b'hand-scissors-o', b'hand-scissors-o'), (b'hand-spock-o', b'hand-spock-o'), (b'hand-stop-o ', b'hand-stop-o '), (b'handshake-o', b'handshake-o'), (b'hard-of-hearing ', b'hard-of-hearing '), (b'hashtag', b'hashtag'), (b'hdd-o', b'hdd-o'), (b'headphones', b'headphones'), (b'heart', b'heart'), (b'heart-o', b'heart-o'), (b'heartbeat', b'heartbeat'), (b'history', b'history'), (b'home', b'home'), (b'hotel ', b'hotel '), (b'hourglass', b'hourglass'), (b'hourglass-1 ', b'hourglass-1 '), (b'hourglass-2 ', b'hourglass-2 '), (b'hourglass-3 ', b'hourglass-3 '), (b'hourglass-end', b'hourglass-end'), (b'hourglass-half', b'hourglass-half'), (b'hourglass-o', b'hourglass-o'), (b'hourglass-start', b'hourglass-start'), (b'i-cursor', b'i-cursor'), (b'id-badge', b'id-badge'), (b'id-card', b'id-card'), (b'id-card-o', b'id-card-o'), (b'image ', b'image '), (b'inbox', b'inbox'), (b'industry', b'industry'), (b'info', b'info'), (b'info-circle', b'info-circle'), (b'institution ', b'institution '), (b'key', b'key'), (b'keyboard-o', b'keyboard-o'), (b'language', b'language'), (b'laptop', b'laptop'), (b'leaf', b'leaf'), (b'legal ', b'legal '), (b'lemon-o', b'lemon-o'), (b'level-down', b'level-down'), (b'level-up', b'level-up'), (b'life-bouy ', b'life-bouy '), (b'life-buoy ', b'life-buoy '), (b'life-ring', b'life-ring'), (b'life-saver ', b'life-saver '), (b'lightbulb-o', b'lightbulb-o'), (b'line-chart', b'line-chart'), (b'location-arrow', b'location-arrow'), (b'lock', b'lock'), (b'low-vision', b'low-vision'), (b'magic', b'magic'), (b'magnet', b'magnet'), (b'mail-forward ', b'mail-forward '), (b'mail-reply ', b'mail-reply '), (b'mail-reply-all ', b'mail-reply-all '), (b'male', b'male'), (b'map', b'map'), (b'map-marker', b'map-marker'), (b'map-o', b'map-o'), (b'map-pin', b'map-pin'), (b'map-signs', b'map-signs'), (b'meh-o', b'meh-o'), (b'microchip', b'microchip'), (b'microphone', b'microphone'), (b'microphone-slash', b'microphone-slash'), (b'minus', b'minus'), (b'minus-circle', b'minus-circle'), (b'minus-square', b'minus-square'), (b'minus-square-o', b'minus-square-o'), (b'mobile', b'mobile'), (b'mobile-phone ', b'mobile-phone '), (b'money', b'money'), (b'moon-o', b'moon-o'), (b'mortar-board ', b'mortar-board '), (b'motorcycle', b'motorcycle'), (b'mouse-pointer', b'mouse-pointer'), (b'music', b'music'), (b'navicon ', b'navicon '), (b'newspaper-o', b'newspaper-o'), (b'object-group', b'object-group'), (b'object-ungroup', b'object-ungroup'), (b'paint-brush', b'paint-brush'), (b'paper-plane', b'paper-plane'), (b'paper-plane-o', b'paper-plane-o'), (b'paw', b'paw'), (b'pencil', b'pencil'), (b'pencil-square', b'pencil-square'), (b'pencil-square-o', b'pencil-square-o'), (b'percent', b'percent'), (b'phone', b'phone'), (b'phone-square', b'phone-square'), (b'photo ', b'photo '), (b'picture-o', b'picture-o'), (b'pie-chart', b'pie-chart'), (b'plane', b'plane'), (b'plug', b'plug'), (b'plus', b'plus'), (b'plus-circle', b'plus-circle'), (b'plus-square', b'plus-square'), (b'plus-square-o', b'plus-square-o'), (b'podcast', b'podcast'), (b'power-off', b'power-off'), (b'print', b'print'), (b'puzzle-piece', b'puzzle-piece'), (b'qrcode', b'qrcode'), (b'question', b'question'), (b'question-circle', b'question-circle'), (b'question-circle-o', b'question-circle-o'), (b'quote-left', b'quote-left'), (b'quote-right', b'quote-right'), (b'random', b'random'), (b'recycle', b'recycle'), (b'refresh', b'refresh'), (b'registered', b'registered'), (b'remove ', b'remove '), (b'reorder ', b'reorder '), (b'reply', b'reply'), (b'reply-all', b'reply-all'), (b'retweet', b'retweet'), (b'road', b'road'), (b'rocket', b'rocket'), (b'rss', b'rss'), (b'rss-square', b'rss-square'), (b's15 ', b's15 '), (b'search', b'search'), (b'search-minus', b'search-minus'), (b'search-plus', b'search-plus'), (b'send ', b'send '), (b'send-o ', b'send-o '), (b'server', b'server'), (b'share', b'share'), (b'share-alt', b'share-alt'), (b'share-alt-square', b'share-alt-square'), (b'share-square', b'share-square'), (b'share-square-o', b'share-square-o'), (b'shield', b'shield'), (b'ship', b'ship'), (b'shopping-bag', b'shopping-bag'), (b'shopping-basket', b'shopping-basket'), (b'shopping-cart', b'shopping-cart'), (b'shower', b'shower'), (b'sign-in', b'sign-in'), (b'sign-language', b'sign-language'), (b'sign-out', b'sign-out'), (b'signal', b'signal'), (b'signing ', b'signing '), (b'sitemap', b'sitemap'), (b'sliders', b'sliders'), (b'smile-o', b'smile-o'), (b'snowflake-o', b'snowflake-o'), (b'soccer-ball-o ', b'soccer-ball-o '), (b'sort', b'sort'), (b'sort-alpha-asc', b'sort-alpha-asc'), (b'sort-alpha-desc', b'sort-alpha-desc'), (b'sort-amount-asc', b'sort-amount-asc'), (b'sort-amount-desc', b'sort-amount-desc'), (b'sort-asc', b'sort-asc'), (b'sort-desc', b'sort-desc'), (b'sort-down ', b'sort-down '), (b'sort-numeric-asc', b'sort-numeric-asc'), (b'sort-numeric-desc', b'sort-numeric-desc'), (b'sort-up ', b'sort-up '), (b'space-shuttle', b'space-shuttle'), (b'spinner', b'spinner'), (b'spoon', b'spoon'), (b'square', b'square'), (b'square-o', b'square-o'), (b'star', b'star'), (b'star-half', b'star-half'), (b'star-half-empty ', b'star-half-empty '), (b'star-half-full ', b'star-half-full '), (b'star-half-o', b'star-half-o'), (b'star-o', b'star-o'), (b'sticky-note', b'sticky-note'), (b'sticky-note-o', b'sticky-note-o'), (b'street-view', b'street-view'), (b'suitcase', b'suitcase'), (b'sun-o', b'sun-o'), (b'support ', b'support '), (b'tablet', b'tablet'), (b'tachometer', b'tachometer'), (b'tag', b'tag'), (b'tags', b'tags'), (b'tasks', b'tasks'), (b'taxi', b'taxi'), (b'television', b'television'), (b'terminal', b'terminal'), (b'thermometer ', b'thermometer '), (b'thermometer-0 ', b'thermometer-0 '), (b'thermometer-1 ', b'thermometer-1 '), (b'thermometer-2 ', b'thermometer-2 '), (b'thermometer-3 ', b'thermometer-3 '), (b'thermometer-4 ', b'thermometer-4 '), (b'thermometer-empty', b'thermometer-empty'), (b'thermometer-full', b'thermometer-full'), (b'thermometer-half', b'thermometer-half'), (b'thermometer-quarter', b'thermometer-quarter'), (b'thermometer-three-quarters', b'thermometer-three-quarters'), (b'thumb-tack', b'thumb-tack'), (b'thumbs-down', b'thumbs-down'), (b'thumbs-o-down', b'thumbs-o-down'), (b'thumbs-o-up', b'thumbs-o-up'), (b'thumbs-up', b'thumbs-up'), (b'ticket', b'ticket'), (b'times', b'times'), (b'times-circle', b'times-circle'), (b'times-circle-o', b'times-circle-o'), (b'times-rectangle ', b'times-rectangle '), (b'times-rectangle-o ', b'times-rectangle-o '), (b'tint', b'tint'), (b'toggle-down ', b'toggle-down '), (b'toggle-left ', b'toggle-left '), (b'toggle-off', b'toggle-off'), (b'toggle-on', b'toggle-on'), (b'toggle-right ', b'toggle-right '), (b'toggle-up ', b'toggle-up '), (b'trademark', b'trademark'), (b'trash', b'trash'), (b'trash-o', b'trash-o'), (b'tree', b'tree'), (b'trophy', b'trophy'), (b'truck', b'truck'), (b'tty', b'tty'), (b'tv ', b'tv '), (b'umbrella', b'umbrella'), (b'universal-access', b'universal-access'), (b'university', b'university'), (b'unlock', b'unlock'), (b'unlock-alt', b'unlock-alt'), (b'unsorted ', b'unsorted '), (b'upload', b'upload'), (b'user', b'user'), (b'user-circle', b'user-circle'), (b'user-circle-o', b'user-circle-o'), (b'user-o', b'user-o'), (b'user-plus', b'user-plus'), (b'user-secret', b'user-secret'), (b'user-times', b'user-times'), (b'users', b'users'), (b'vcard ', b'vcard '), (b'vcard-o ', b'vcard-o '), (b'video-camera', b'video-camera'), (b'volume-control-phone', b'volume-control-phone'), (b'volume-down', b'volume-down'), (b'volume-off', b'volume-off'), (b'volume-up', b'volume-up'), (b'warning ', b'warning '), (b'wheelchair', b'wheelchair'), (b'wheelchair-alt', b'wheelchair-alt'), (b'wifi', b'wifi'), (b'window-close', b'window-close'), (b'window-close-o', b'window-close-o'), (b'window-maximize', b'window-maximize'), (b'window-minimize', b'window-minimize'), (b'window-restore', b'window-restore'), (b'wrench', b'wrench')], label=b'Icon', required=False)), (b'title', wagtail.wagtailcore.blocks.CharBlock(label=b'Title', max_length=50)), (b'content', wagtail.wagtailcore.blocks.RichTextBlock(label=b'Content'))]), icon=b'list-ol', template=b'cartoview_cms/streamfields/vertical_tab.html')), (b'image_text_overlay', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(label=b'Image')), (b'text', wagtail.wagtailcore.blocks.CharBlock(label=b'Text', max_length=200))]), icon=b'fa-image', template=b'cartoview_cms/streamfields/image_text_overlay.html')), (b'image_gallery', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock(), icon=b'image', label=b'Image'))]), icon=b'fa-camera-retro', template=b'cartoview_cms/streamfields/image_gallery.html'))], blank=True),
        ),
    ]
