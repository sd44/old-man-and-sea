# Implements use of bib2gls with glossaries-extra.
# Version of 4 Feb 2024.
# Thanks to Marcel Ilg for a suggestion.

# !!! ONLY WORKS WITH VERSION 4.54 or higher of latexmk

push @generated_exts, 'glstex', 'glg';

# For case that \GlsXtrLoadResources is used and so glstex file (first one)
# has same name as .aux file.
add_cus_dep('aux', 'glstex', 0, 'run_bib2gls');

# For case that \glsxtrresourcefile is used and so glstex file (first one)
# has same name as .bib file.
add_cus_dep('bib', 'glstex', 0, 'run_bib2gls_alt');

sub run_bib2gls {
    my $ret = 0;
    if ( $silent ) {
        $ret = system "bib2gls --silent --group '$_[0]'";
    } else {
        $ret = system "bib2gls --group '$_[0]'";
    };

    # bib2gls puts output files in current directory.
    # At least put main glstex in same directory as aux file to satisfy
    # definition of custom dependency.
    my ($base, $path) = fileparse( $_[0] );
    if ($path && -e "$base.glstex") {
        rename "$base.glstex", "$path$base.glstex";
    }

    if ($ret) {
        warn "Run_bib2gls: Error, so I won't analyze .glg file\n";
        return $ret;
    }
    # Analyze log file.
    my $log = "$_[0].glg";
    if ( open( my $log_fh, '<', $log) ) {
        while (<$log_fh>) {
            s/\s*$//;
            if (/^Reading\s+(.+)$/) { rdb_ensure_file( $rule, $1 ); }
            if (/^Writing\s+(.+)$/) { rdb_add_generated( $1 ); }
        }
        close $log_fh;
    }
    else {
        warn "Run_bib2gls: Cannot read log file '$log': $!\n";
    }
    return $ret;
}

sub run_bib2gls_alt {
    return Run_subst( 'internal run_bib2gls %Y%R' );
}


$pdf_mode = 5; # 5为xelatex
$xelatex = "xelatex -file-line-error -halt-on-error -shell-escape -no-pdf -synctex=1 %O %S";
$postscript_mode = $dvi_mode = 0;

$clean_ext = 'thm glo gls bbl hd loe synctex.gz xdv run.xml inx idx ilg tdo aux bbl bbl-SAVE-ERROR bcf bcf-SAVE-ERROR blg log fdb_latexmk fls toc rel lof lot bak';


$pdf_previewer = 'okular %O %S';
#$preview_continuous_mode = 1; # equivalent to -pvc

$preview_mode = 1; # equivalent to -pv
