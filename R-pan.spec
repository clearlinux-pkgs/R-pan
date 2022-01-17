#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pan
Version  : 1.6
Release  : 6
URL      : https://cran.r-project.org/src/contrib/pan_1.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pan_1.6.tar.gz
Summary  : Multiple Imputation for Multivariate Panel or Clustered Data
Group    : Development/Tools
License  : GPL-3.0
Requires: R-pan-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
generalized linear mixed models and Gibbs sampler for multivariate linear
              mixed models with incomplete data, as described in Schafer JL (1997)
              "Imputation of missing covariates under a multivariate linear mixed model".
              Technical report 97-04, Dept. of Statistics, The Pennsylvania State University.

%package lib
Summary: lib components for the R-pan package.
Group: Libraries

%description lib
lib components for the R-pan package.


%prep
%setup -q -c -n pan
cd %{_builddir}/pan

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642444526

%install
export SOURCE_DATE_EPOCH=1642444526
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pan
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pan
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pan
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc pan || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pan/CITATION
/usr/lib64/R/library/pan/DESCRIPTION
/usr/lib64/R/library/pan/INDEX
/usr/lib64/R/library/pan/Meta/Rd.rds
/usr/lib64/R/library/pan/Meta/data.rds
/usr/lib64/R/library/pan/Meta/features.rds
/usr/lib64/R/library/pan/Meta/hsearch.rds
/usr/lib64/R/library/pan/Meta/links.rds
/usr/lib64/R/library/pan/Meta/nsInfo.rds
/usr/lib64/R/library/pan/Meta/package.rds
/usr/lib64/R/library/pan/Meta/vignette.rds
/usr/lib64/R/library/pan/NAMESPACE
/usr/lib64/R/library/pan/R/pan
/usr/lib64/R/library/pan/R/pan.rdb
/usr/lib64/R/library/pan/R/pan.rdx
/usr/lib64/R/library/pan/data/Rdata.rdb
/usr/lib64/R/library/pan/data/Rdata.rds
/usr/lib64/R/library/pan/data/Rdata.rdx
/usr/lib64/R/library/pan/data/datalist
/usr/lib64/R/library/pan/doc/index.html
/usr/lib64/R/library/pan/doc/pan-tr.Rnw
/usr/lib64/R/library/pan/doc/pan-tr.pdf
/usr/lib64/R/library/pan/help/AnIndex
/usr/lib64/R/library/pan/help/aliases.rds
/usr/lib64/R/library/pan/help/pan.rdb
/usr/lib64/R/library/pan/help/pan.rdx
/usr/lib64/R/library/pan/help/paths.rds
/usr/lib64/R/library/pan/html/00Index.html
/usr/lib64/R/library/pan/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/pan/libs/pan.so
/usr/lib64/R/library/pan/libs/pan.so.avx2
/usr/lib64/R/library/pan/libs/pan.so.avx512
