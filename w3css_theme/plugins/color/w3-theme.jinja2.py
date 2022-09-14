.w3-theme-l5 {color:{{ color_l5 }} !important; background-color:{{ bgcolor_l5 }} !important}
.w3-theme-l4 {color:{{ color_l4 }} !important; background-color:{{ bgcolor_l4 }} !important}
.w3-theme-l3 {color:{{ color_l3 }} !important; background-color:{{ bgcolor_l3 }} !important}
.w3-theme-l2 {color:{{ color_l2 }} !important; background-color:{{ bgcolor_l2 }} !important}
.w3-theme-l1 {color:{{ color_l1 }} !important; background-color:{{ bgcolor_l1 }} !important}

.w3-theme-dark {color:{{ color_d5 }} !important; background-color:{{ bgcolor_d5 }} !important}
.w3-theme-light {color:{{ color_l5 }} !important; background-color:{{ bgcolor_l5 }} !important}
.w3-theme-action {color:{{ color_d5 }} !important; background-color:{{ bgcolor_d5 }} !important}

.w3-theme {color:{{ color_theme_l }} !important; background-color:{{ bgcolor_theme }} !important}
.w3-text-theme {color:{{ bgcolor_theme }} !important}
.w3-border-theme {border-color:{{ bgcolor_theme }} !important}

.w3-hover-theme:hover {color:{{ color_theme_l }} !important; background-color:{{ bgcolor_theme }} !important}
.w3-hover-text-theme:hover {color:{{ bgcolor_theme }} !important}
.w3-hover-border-theme:hover {border-color:{{ bgcolor_theme }} !important}
pre {
  color:{{ color_l4 }};
  background-color:{{ bgcolor_l4 }};
  border-left:4px solid {{ bgcolor_theme }};
}
code {
  background-color:{{ bgcolor_l4 }};
}
a{color:{{ bgcolor_theme }} !important}
table tbody tr:hover,table li:hover{
    background-color:{{ bgcolor_l3 }}
}

.footer a{color:{{ color_theme_l }} !important}


@media (prefers-color-scheme: dark) {
  .w3-theme-l1 {color:{{ color_d1 }} !important; background-color:{{ bgcolor_d1 }} !important}
  .w3-theme-l2 {color:{{ color_d2 }} !important; background-color:{{ bgcolor_d2 }} !important}
  .w3-theme-l3 {color:{{ color_d3 }} !important; background-color:{{ bgcolor_d3 }} !important}
  .w3-theme-l4 {color:{{ color_d4 }} !important; background-color:{{ bgcolor_d4 }} !important}
  .w3-theme-l5 {color:{{ color_d5 }} !important; background-color:{{ bgcolor_d5 }} !important}

  .w3-theme-dark {color:{{ color_l5 }} !important; background-color:{{ bgcolor_l5 }} !important}
  .w3-theme-light {color:{{ color_d5 }} !important; background-color:{{ bgcolor_d5 }} !important}
  .w3-theme-action {color:{{ color_d5 }} !important; background-color:{{ bgcolor_d5 }} !important}

  .w3-theme {color:{{ color_theme_d }} !important; background-color:{{ bgcolor_theme }} !important}
  .w3-text-theme {color:{{ bgcolor_theme }} !important}
  .w3-border-theme {border-color:{{ bgcolor_theme }} !important}

  .w3-hover-theme:hover {color:{{ color_theme_d }} !important; background-color:{{ bgcolor_theme }} !important}
  .w3-hover-text-theme:hover {color:{{ bgcolor_theme }} !important}
  .w3-hover-border-theme:hover {border-color:{{ bgcolor_theme }} !important}
  pre {
    color:{{ color_d4 }};
    background-color:{{ bgcolor_d4 }};
    border-left:4px solid {{ bgcolor_theme }};
  }
  code {
    background-color:{{ bgcolor_d4 }};
  }
  a{color:{{ bgcolor_theme }} !important}
  table tbody tr:hover,table li:hover{
    background-color:{{ bgcolor_d3 }}
  }
  
  .footer a{color:{{ color_theme_d }} !important}
}