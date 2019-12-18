\t on
\pset format unaligned
select json_agg(t) from (select name, continent_name, wiki_extract from countries) as t;

