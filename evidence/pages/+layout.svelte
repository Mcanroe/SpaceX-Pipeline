<script>
	import '@evidence-dev/tailwind/fonts.css';
	import '../app.css';
	import { EvidenceDefaultLayout } from '@evidence-dev/core-components';
	export let data;
</script>

<EvidenceDefaultLayout {data} neverShowQueries githubRepo=https://github.com/Mcanroe/SpaceX-Pipeline builtWithEvidence=false>
	<slot slot="content" />
</EvidenceDefaultLayout>
