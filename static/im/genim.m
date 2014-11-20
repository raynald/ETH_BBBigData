num_im = 300;
value = zeros(num_im, 3);
for k = 1:3
    value(:, k) = linspace(0, 255, num_im);
    value(:, k) = value(randperm(length(value) ), k);
end
edge_size = 3;
im = zeros(edge_size, edge_size, 3);
for k = 1:num_im
    for l = 1:3
        im(:,:, l) = ones(edge_size, edge_size) * value(k, l);
    end
    imwrite(uint8(im), ['../images/', num2str(k), '.jpg'], 'jpg');
end
