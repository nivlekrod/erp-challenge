do
$$
    declare
        maior_id integer;
    begin
        select coalesce(max(id), 1)
        into maior_id
        from sale;
        perform setval('sale_id_seq', maior_id);
        raise
            notice 'Sucesso! A sequence sale_id_seq foi atualizada para %', maior_id;
    end;
$$