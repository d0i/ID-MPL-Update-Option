IDTemplate
==========

Template Repository for I-D Edit Task

This expects following xml2rfc installed (current debian version will not work).
http://svn.tools.ietf.org/svn/tools/xml2rfc/trunk/ 

If you found pandoc2rfc is missing, please add it as extenal submodule with

% git submodule add https://github.com/miekg/pandoc2rfc.git ext/pandoc2rfc 

However, current xml2rfc doesn't work well with pandoc2rfc style XML import. Ad-hoc patched version to use older version is in the following repo. (for example, debian's packaged version is 1.36) 

% git submodule add https://github.com/miekg/pandoc2rfc.git ext/pandoc2rfc 

