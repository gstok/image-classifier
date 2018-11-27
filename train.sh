python retrain.py \
--image_dir ./images/ \
--how_many_training_steps 10000 \
--bottleneck_dir ./result/bottleneck/ \
--output_labels ./result/output_labels.txt \
--summaries_dir ./result/retrain_logs/ \
--output_graph ./result/output_graph.pb \
--intermediate_output_graphs_dir ./result/intermediate_graph/ \
--saved_model_dir ./result/model/

